from Graph.GLocation import GLocation


class Agent:

    def __init__(self, id: int, value: float, src: int, dest: int, speed: float, pos: str):
        self.id = id
        self.tag = 0
        self.value = value
        self.src = src
        self.dest = dest
        self.speed = speed
        temp_pos = pos.split(",")
        t_pos = (float(temp_pos[0]), float(temp_pos[1]), float(temp_pos[2]))
        self.pos = GLocation(t_pos)
        self.location = pos


