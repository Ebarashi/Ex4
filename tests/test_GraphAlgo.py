from unittest import TestCase

from Graph.DiGraph import DiGraph
from Graph.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    g1: GraphAlgo = GraphAlgo()

    def test_shortest_path(self):
        g = self.simple_graph()
        ga = GraphAlgo(g)
        self.assertTupleEqual((3.0, [1, 2, 3, 7]), ga.shortest_path(1, 7))
        self.assertEqual((float('inf'), []), ga.shortest_path(1, 88))
        self.assertEqual((9.0, [3, 7, 8, 9]), ga.shortest_path(3, 9))


    def test_center_point(self):
        g = self.simple_graph()
        ga = GraphAlgo(g)
        self.assertTupleEqual((None, float('inf')), ga.centerPoint())

    @staticmethod
    def simple_graph():
        g = DiGraph()
        for i in range(10):
            g.add_node(i)

        for i in range(10):
            g.add_edge(i, 10 - i, i * 0.5)
            g.add_edge(i, i + 1, i * 0.5)
        return g
