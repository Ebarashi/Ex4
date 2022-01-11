from unittest import TestCase
from Game.Main import Main
from tests.MyClient import MyClient


class Game(TestCase):

    def test_load_pokemons(self):
        self.client = MyClient()
        self.game = Main(self.client)
        self.game.load_pokemon()
        self.assertEqual(1, len(self.game.pokemons))
        self.assertEqual(5, self.game.pokemons[0].value)  # value = 5.0
        self.assertEqual(-1, self.game.pokemons[0].type)  # type = -1

    def test_load_agents(self):
        self.client = MyClient()
        self.game = Main(self.client)
        self.game.load_agents()
        self.assertEqual(1, len(self.game.agents))
        self.assertEqual(0, self.game.agents[0].id)
        self.assertEqual(1, self.game.agents[0].speed)


    def test_load(self):
        self.client = MyClient()
        self.game = Main(self.client)
        self.game.load_info()
        self.assertEqual(1, self.game.info.agents)

    def test_load_info(self):
        self.client = MyClient()
        self.game = Main(self.client)
        self.game.load_info()
        self.assertEqual(1, self.game.info.agents)
        self.assertEqual(1, self.game.info.pokemons)

    def test_add_agents(self):
        self.client = MyClient()
        self.game = Main(self.client)
        self.game.load_agents()
        self.assertEqual(1, len(self.game.agents))
        self.assertEqual(0, self.game.agents[0].id)
