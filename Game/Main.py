import json
import math
import queue
from Game.Info import Info
from client_python.client import Client
from Game.Pokemon import Pokemon
from Game.Agent import Agent
from Graph.GraphAlgo import GraphAlgo


class Main:

    def __init__(self, client: Client):

        self.client = client
        self.total_time = 0
        self.agents = []
        self.info: Info = None
        self.pokemons = []
        self.load_info()
        self.gA = GraphAlgo()
        self.gA.load_from_json('../' + self.info.graph)
        self.add_agents()

    # load the agents
    def load_agents(self):

        json_agent = json.loads(self.client.get_agents())
        self.agents = []
        for a in json_agent["Agents"]:
            new_agent = Agent(**a["Agent"])
            self.agents.append(new_agent)

    def add_agents(self):

        self.load_pokemons()
        center = self.gA.centerPoint()
        q = queue.PriorityQueue()

        for pok in self.pokemons:
            q.put(pok)

        for i in range(self.info.agents):
            if self.info.agents == 1 and self.info.pokemons > 3:
                self.client.add_agent("{\"id\":" + str(center[0]) + "}")
            elif not q.empty():
                pok: Pokemon = q.get()
                self.client.add_agent("{\"id\":" + str(pok.edge[0]) + "}")

    # load game info
    def load_info(self):

        json_info = json.loads(self.client.get_info())
        self.info = Info(**json_info["GameServer"])

    # load the pokemons
    def load_pokemons(self):

        json_pokemons = json.loads(self.client.get_pokemons())
        self.pokemons = []
        for p in json_pokemons["Pokemons"]:
            po = Pokemon(**p["Pokemon"])
            g = self.gA.graph
            po.find_location(g)
            self.pokemons.append(po)

    def load_all(self):
        self.load_info()
        self.load_agents()
        self.load_pokemons()

    def allocate(self):
        """
        Go through all the agents, in case one of the agents on a node,
        the function sends it to a function that will allocate the nearest
        pokemon and update the agent's dest accordingly.
        """
        self.load_all()
        self.total_time = 0
        for agent in self.agents:
            if agent.dest == -1:
                self.allocate_pok(agent)

    def allocate_pok(self, agent: Agent):
        #
        """
        The function receives an agent and allocates to him the pokemon that the most closer to him and updates the
        agent's dest accordingly. pokemon that all ready grabbed will not allocate again then return to the server by
        the client function the next move the agent need to do in order to get the pokemon dest
        """
        min_time: float = math.inf
        next_edge: int = -1
        p_ans = None

        for p in self.pokemons:
            if not p.grab:
                temp_dist, path = self.gA.shortest_path(agent.src, p.edge[0])
                time_travel = temp_dist / agent.speed
                if time_travel < min_time:
                    min_time = time_travel
                    p_ans = p
                    if min_time == 0:
                        next_edge = p.edge[1]
                    else:
                        next_edge = path[1]
        self.total_time += min_time
        if p_ans is not None:
            if not p_ans.grab:
                p_ans.grab = True
        self.client.choose_next_edge('{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_edge) + '}')


