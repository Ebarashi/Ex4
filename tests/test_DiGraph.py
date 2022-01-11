from unittest import TestCase

from Graph.DiGraph import DiGraph
from Graph.Edge import Edge
from Graph.Node import Node


class TestDiGraph(TestCase):
    g = DiGraph()
    n1 = Node(0, (0, 0, 0))
    n2 = Node(1, (1, 1, 1))
    n3 = Node(2, (2, 2, 2))
    e1 = Edge(0, 1, 1.5)
    e2 = Edge(0, 2, 2.0)
    e3 = Edge(1, 0, 3.5)

    def test_v_size(self):
        self.assertEqual(0, self.g.v_size())
        self.g.add_node(self.n1.key, (0, 0, 0))
        self.assertEqual(1, self.g.v_size())
        self.g.remove_node(self.n1.key)
        self.assertEqual(0, self.g.v_size())

    def test_e_size(self):
        self.g = DiGraph()
        self.g.add_node(self.n1.key, (0, 0, 0))
        self.g.add_node(self.n2.key, (1, 1, 1))
        self.g.add_node(self.n3.key, (2, 2, 2))
        self.assertEqual(0, self.g.e_size())
        self.g.add_edge(self.n1.key, self.n2.key, 20)
        self.assertEqual(1, self.g.e_size())
        self.g.remove_edge(self.n1.key, self.n2.key)
        self.assertEqual(0, self.g.e_size())

    def test_get_all_v(self):
        self.g = DiGraph()
        self.g.add_node(self.n1.key, (0, 0, 0))
        self.g.add_node(self.n2.key, (1, 1, 1))
        expected = "{0: (0, pos(0, 0, 0)), 1: (1, pos(1, 1, 1))}"
        self.assertEqual(expected, str(self.g.get_all_v()))

    def test_all_in_edges_of_node(self):
        self.g = DiGraph()
        self.g.add_node(self.n1.key, (0, 0, 0))
        self.g.add_node(self.n2.key, (1, 1, 1))
        self.g.add_edge(0, 1, 20)
        self.g.add_edge(1, 0, 10)
        expected = "{1: Edge{src= 1, dest= 0, weight= 10}}"
        self.assertEqual(expected, str(self.g.all_in_edges_of_node(self.n1.key)))

    def test_all_out_edges_of_node(self):
        self.g = DiGraph()
        self.g.add_node(self.n1.key, (0, 0, 0))
        self.g.add_node(self.n2.key, (1, 1, 1))
        self.g.add_edge(0, 1, 20)
        self.g.add_edge(1, 0, 10)
        expected = "{1: Edge{src= 0, dest= 1, weight= 20}}"
        self.assertEqual(expected, str(self.g.all_out_edges_of_node(self.n1.key)))

    def test_get_mc(self):
        self.g = DiGraph()
        self.assertEqual(0, self.g.MC)
        self.g.add_node(self.n1.key, (0, 0, 0))
        self.g.add_node(self.n2.key, (1, 1, 1))
        self.g.add_edge(self.n1.key, self.n2.key, 3)
        self.g.remove_edge(self.n1.key, self.n2.key)
        self.g.remove_node(self.n1.key)
        self.g.remove_node(self.n2.key)
        self.assertEqual(6, self.g.MC)

    def test_add_edge(self):
        self.g = DiGraph()
        self.g.add_node(self.n1.key, (0, 0, 0))
        self.g.add_node(self.n2.key, (1, 1, 1))
        self.g.add_edge(self.n1.key, self.n2.key, 20)
        self.g.add_edge(self.n2.key, self.n1.key, 10)
        self.assertEqual(2, self.g.e_size())

    def test_add_node(self):
        self.g = DiGraph()
        self.assertEqual(0, self.g.v_size())
        self.g.add_node(self.n1.key, (0, 0, 0))
        self.g.add_node(self.n2.key, (1, 1, 1))
        self.assertEqual(2, self.g.v_size())

    def test_getnode(self):
        self.g = DiGraph()
        self.g.add_node(self.n1.key, (0, 0, 0))
        self.g.add_node(self.n2.key, (1, 1, 1))
        node1 = self.g.getnode(0)
        self.assertEqual(self.n1.key, node1.key)
        self.assertEqual(repr(self.n1.location), repr(node1.location))
        self.assertEqual(self.n1.weight, node1.weight)

    def test_remove_node(self):
        self.g = DiGraph()
        self.g.add_node(self.n1.key, (0, 0, 0))
        self.g.add_node(self.n2.key, (1, 1, 1))
        self.g.add_edge(self.n1.key, self.n2.key, 21)
        self.g.add_edge(self.n2.key, self.n1.key, 18)
        self.assertEqual(2, self.g.e_size())
        self.g.remove_node(self.n1.key)
        self.assertEqual(1, self.g.v_size())
        self.assertEqual(1, self.g.e_size())

    def test_remove_edge(self):
        self.g = DiGraph()
        self.g.add_node(self.n1.key, (0, 0, 0))
        self.g.add_node(self.n2.key, (1, 1, 1))
        self.g.add_edge(self.n1.key, self.n2.key, 21.3)
        self.g.add_edge(self.n2.key, self.n1.key, 14.7)
        self.assertEqual(2, self.g.e_size())
        self.g.remove_edge(self.n1.key, self.n2.key)
        self.assertEquals(1, self.g.e_size())
