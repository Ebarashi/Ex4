from unittest import TestCase

from Graph.GLocation import GLocation


class TestGlocation(TestCase):

    def test_distance(self):
        x = GLocation((0,0,0))
        y = GLocation((3,3,0))

        self.assertEqual(x.distance(y),4.242640687119285)
