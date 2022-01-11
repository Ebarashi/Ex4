class MyClient:
    def __init__(self):
        self.agents: str = """
                        {
                            "Agents":[
                                {
                                    "Agent":
                                    {
                                        "id":0,
                                        "value":0.0,
                                        "src":0,
                                        "dest":1,
                                        "speed":1.0,
                                        "pos":"35.18753053591606,32.10378225882353,0.0"
                                    }
                                }
                            ]
                        }
                        """
        self.info: str = """
                        {
                            "GameServer":{
                                "pokemons":1,
                                "is_logged_in":false,
                                "moves":1,
                                "grade":0,
                                "game_level":0,
                                "max_user_level":-1,
                                "id":0,
                                "graph":"data/A0",
                                "agents":1
                            }
                        }
                        """
        self.pokemons = """
                        {
                            "Pokemons":[
                                {
                                    "Pokemon":{
                                        "value":5.0,
                                        "type":-1,
                                        "pos":"35.197656770719604,32.10191878639921,0.0"
                                    }
                                }
                            ]
                        }
                        """

    def get_pokemons(self):
        return self.pokemons

    def get_info(self):
        return self.info

    def get_agents(self):
        return self.agents

    def add_agent(self, str_agent):
        return str_agent
