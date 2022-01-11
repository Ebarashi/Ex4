from Graph.GraphInterface import GraphInterface
from Graph.Edge import Edge
from Graph.Node import Node


class DiGraph(GraphInterface):

    def __init__(self):
        super().__init__()
        self.nodes = {}
        self.edges = {}
        self.SizeOfEdge = 0
        self.MC = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.SizeOfEdge

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        ans = {}
        for i in self.edges.keys():
            for j in self.edges[i].keys():
                if j == id1:
                    if i not in ans.keys():
                        ans[i] = self.edges.get(i).get(j)
        return ans

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.edges[id1]

    def get_mc(self) -> int:
        return self.MC

    # id1 - src , id2 - dst
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.nodes.keys() or id2 not in self.nodes.keys():
            return False
        edge = Edge(id1, id2, weight)
        if id1 in self.edges.keys():
            if id2 in self.edges[id1].keys():
                if self.edges[id1][id2].weight != weight:
                    self.edges[id1][id2].weight = weight
                return False
            else:
                self.edges[id1][id2] = edge
                self.SizeOfEdge += 1
        else:
            edge = Edge(id1, id2, weight)
            self.edges[id1] = {id2: edge}
            self.SizeOfEdge += 1

        self.MC += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes.keys():
            return False
        # else:
        #     if pos is None:
        #         pos = GLocation(None)
        self.nodes[node_id] = Node(node_id, pos)

        self.MC = self.MC + 1
        return True

    def getnode(self, id: int) -> Node:
        return self.nodes[id]

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes.keys():
            return False
        else:
            self.nodes.pop(node_id)

        if node_id in self.edges.keys():
            self.edges.pop(node_id)

        for id1 in self.edges.keys():
            for id2 in self.edges.get(id1):
                if id2 == node_id:
                    self.edges.get(id1).pop(node_id)
                    self.SizeOfEdge -= 1
                    break

        self.MC += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self.edges.keys():
            return False
        if node_id1 in self.edges.keys() and node_id2 not in self.edges[node_id1].keys():
            return False
        else:
            self.edges[node_id1].pop(node_id2)
            self.SizeOfEdge -= 1
        self.MC = self.MC + 1
        return True

    def __str__(self):
        return "Graph: |V|= " + str(self.v_size()) + ", |E|= " + str(self.SizeOfEdge)

    def __repr__(self):
        return "Graph: |V|= " + str(self.v_size()) + ", |E|= " + str(self.SizeOfEdge)
