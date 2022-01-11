import math
from random import random, randint


class GLocation:

    def __init__(self, pos):
        if pos is None:
            self.x = randint(35185, 35215) / 1000
            self.y = randint(32101, 32108) / 1000
            self.z = 0.0
        else:
            self.x = pos[0]
            self.y = pos[1]
            self.z = pos[2]

    def distance(self, other):
        tempx = math.pow((self.x - other.x), 2)
        tempy = math.pow((self.y - other.y), 2)
        tempz = math.pow((self.z - other.z), 2)
        return math.sqrt((tempx + tempy + tempz))

    def __str__(self):
        return "[" + self.x + ", " + self.y + ", " + self.z + "]"

    def __repr__(self):
        return f"pos{self.x, self.y, self.z}"
