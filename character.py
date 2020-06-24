from typing import List, Dict

from item import Item
from utils.enums import ABILITY
from utils.roll import roll_standard_table


class Character(object):
    def __init__(self, *, init_rolls=None, items: List[Item] = None, name='-=>NONAME<=-'):
        self.name = name
        if not init_rolls:
            init_rolls = roll_standard_table()
        self.abilities: Dict[ABILITY, Ability] = \
            {ability: Ability(name=ability, base=init_rolls[i]) for i, ability in enumerate(ABILITY)}
        self.items = items if items else []


class Ability(object):
    def __init__(self, *, name=None, base=0):
        self.max = 20
        self.score = base
        self.user_override = None
        self.base = base
        self.name = name

    def __repr__(self):
        s = f"{self.__class__.__name__}("
        for k, v in self.__dict__.items():
            s += f"{k}={v}, "
        s += "\b\b)"
        return s
