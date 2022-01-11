import json
import math
import queue
from Game.Info import Info
from client_python.client import Client
from Pokemon import Pokemon
from Game.Agent import Agent
from Graph.GraphAlgo import GraphAlgo


class Main:

    def __init__(self, client: Client):

        self.client = client
        self.total_time = 0
        self.info: Info = None
        self.pokemons = []
        self.agents = []
        self.load_info()
        self.graphAlgo = GraphAlgo()
        self.graphAlgo.load_from_json('../' + self.info.graph)
        self.add_agents()

    # the function update the info, the agents list, and the pokemons list.
    def load(self):
        self.load_info()
        self.load_agent()
        self.load_pokemon()

    def allocate(self):
        """
        Go through all the agents, in case one of the agents is at rest,
        the function sends it to a function that will locate the nearest
        Pokemon and update the agent's destination accordingly.
        """
        self.load()
        self.total_time = 0
        for agent in self.agents:
            if agent.dest == -1:
                self.allocate_pok(agent)

    def allocate_pok(self, agent: Agent):
        #
        """
        The function receives an agent and locates to him the pokemon
        that the most closer to him and updates the agent's dest accordingly.
        pokemon that all ready grabbed will not allocate again
        then return to the client function the next move the agent need to do in order to get the pokemon dest
        :param agent:
        """
        min_time: float = math.inf
        next_edge: int = -1
        p_ans = None

        for p in self.pokemons:
            if not p.grab:
                temp_dist, path = self.graphAlgo.shortest_path(agent.src, p.edge[0])
                time_travel = temp_dist / agent.speed
                if time_travel < min_time:
                    min_time = time_travel
                    p_ans = p
                    if min_time == 0:
                        next_edge = p.edge[1]
                    else:
                        next_edge = path[1]
        self.total_time += min_time
        # if p_ans.value != -1:
        #     self.pokemons.remove(p_ans)
        if p_ans is not None:
            if not p_ans.grab:
                p_ans.grab = True
        if agent.src == p_ans.edge[0]:
            self.client.move()
        self.client.choose_next_edge('{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_edge) + '}')

    def add_agents(self):

        self.load_pokemon()
        center = self.graphAlgo.centerPoint()
        q = queue.PriorityQueue()

        for pok in self.pokemons:
            q.put(pok)

        for i in range(self.info.agents):
            if self.info.agents == 1 and self.info.pokemons > 3:
                self.client.add_agent("{\"id\":" + str(center[0]) + "}")
            if not q.empty():
                pok: Pokemon = q.get()
                self.client.add_agent("{\"id\":" + str(pok.edge[0]) + "}")

    # load game info
    def load_info(self):

        json_info = json.loads(self.client.get_info())
        self.info = Info(**json_info["GameServer"])

    # load the pokemons
    def load_pokemon(self):

        json_pokemons = json.loads(self.client.get_pokemons())
        self.pokemons = []
        for p in json_pokemons["Pokemons"]:
            po = Pokemon(**p["Pokemon"])
            g = self.graphAlgo.graph
            po.find_location(g)
            self.pokemons.append(po)

    # load the agents
    def load_agent(self):

        json_agent = json.loads(self.client.get_agents())
        self.agents = []
        for a in json_agent["Agents"]:
            new_agent = Agent(**a["Agent"])
            self.agents.append(new_agent)
