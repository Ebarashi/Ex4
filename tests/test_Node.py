import sys
from unittest import TestCase

from Graph.Node import Node


class TestNode(TestCase):

    def test_node(self):
        self.node1 = Node(0, (32.1232346, 35.3456645, 0.0))

        self.assertEqual(32.1232346, self.node1.location.x)
        self.assertEqual(35.3456645, self.node1.location.y)

        self.assertEqual(0, self.node1.key)
        self.assertEqual(-1, self.node1.tag)
        self.assertEqual(sys.float_info.max, self.node1.weight)
        self.assertEqual("white", self.node1.info)


