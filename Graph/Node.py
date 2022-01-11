import sys

from Graph.GLocation import GLocation


class Node:
    startKeys = 0

    def __init__(self, key: int, location: tuple):
        # if key is None:
        #     self.key = Node.startKeys
        #     Node.startKeys += 1
        # else:
        self.key = key
        # Node.startKeys += 1
        self.location = GLocation(location)
        self.weight = sys.float_info.max
        self.info = "white"
        self.tag = -1

    # def __str__(self):
    #     # return "Node{key= "+self.key+ ", weight= "+self.weight +", info= "+self.info+", tag= "+self.tag+"}"
    #     return "Node{key= " + self.key + "}"

    def __repr__(self):
        return f"{self.key, self.location}"


