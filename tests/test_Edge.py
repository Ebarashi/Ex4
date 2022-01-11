from unittest import TestCase

from Graph.Edge import Edge


class TestEdge(TestCase):

    def test_edge(self):
        self.edge1 = Edge(0, 1, 435)
        self.assertEqual(0, self.edge1.src)
        self.assertEqual(1, self.edge1.dst)
        self.assertEqual(435, self.edge1.weight)
