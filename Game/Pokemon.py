import math
import sys

import pygame

from Graph.DiGraph import DiGraph
from Graph.GLocation import GLocation


def distance(src: GLocation, dest: GLocation):
    d = math.sqrt((src.x - dest.x) ** 2 + (src.y - dest.y) ** 2)
    return d


class Pokemon:

    def __init__(self, value: float, type: int, pos: str):
        self.value = value
        self.type = type
        temp_pos = pos.split(",")
        t_pos = (float(temp_pos[0]), float(temp_pos[1]), float(temp_pos[2]))
        self.pos = GLocation(t_pos)
        self.grab = False
        self.edge = ()

    def __lt__(self, pokemon):
        return self.value < pokemon.value

    def find_location(self, graph: DiGraph):
        # -> (int, int)
        for src in graph.nodes.keys():
            for dest in graph.all_out_edges_of_node(src).keys():
                if self.is_between(src, dest, graph):
                    self.edge = src, dest
                    # return src, dest

        # return -1, -1

    def is_between(self, src: int, dest: int, graph: DiGraph) -> bool:

        if self.type < 0 and src < dest:
            return False

        if self.type > 0 and src > dest:
            return False

        src_loc = graph.nodes.get(src).location
        dest_loc = graph.nodes.get(dest).location

        edge_len: float = distance(src_loc, dest_loc)
        pokemon_dist: float = distance(src_loc, self.pos) + distance(dest_loc, self.pos)

        return abs(edge_len - pokemon_dist) < 0.0000001
