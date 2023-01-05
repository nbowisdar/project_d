import json
import random


def _load_agents() -> list[str]:
    with open('agents_data.json', 'r', encoding='utf-8') as file:
        return json.load(file)['agents']


class FakeAgent:
    def __init__(self):
        self.__agents = _load_agents()

    def random(self) -> str:
        return random.choice(self.__agents)