from collections import namedtuple
from typing import List, Dict

from item import Item
from item.components.score_manipulator import ScoreChanger, ScoreSetter, ScoreMaxSetter
from utils.enums import ABILITY
from utils.roll import roll_standard_table


class Character(object):
    def __init__(self, *, init_rolls=None, items: List[Item] = None, name='-=>NONAME<=-'):
        self.name = name
        if not init_rolls:
            init_rolls = roll_standard_table()
        for i, ab in enumerate(ABILITY):
            self.abilities: Dict[ABILITY, Ability] = {ability: Ability(name=ability, base=init_rolls[i])
                                                      for i, ability in enumerate(ABILITY)}
        self.items = items


class AbilityOverseer(object):
    def __init__(self, char_sheet: Character):
        self._abilities = char_sheet.abilities
        self._items = char_sheet.items

    def get_manipulators(self):
        score_setters = namedtuple('ScoreSetters', ['score_setters'])(score_setters=[])
        max_setters = namedtuple('MaxSetters', ['max_setters'])(max_setters=[])
        score_changers = namedtuple('ScoreChangers', ['score_changers'])(score_changers=[])
        for ability_name, ability in self._abilities.items():
            for item in self._items:
                for component in item.components.values():
                    if type(component) == ScoreSetter and component.ability == ability_name:
                        score_setters.score_setters.append(component)
                    elif type(component) == ScoreMaxSetter and component.ability == ability_name:
                        max_setters.max_setters.append(component)
                    elif type(component) == ScoreChanger and component.ability == ability_name:
                        score_changers.score_changers.append(component)
        return score_setters, max_setters, score_changers

    def calculate(self):
        for ability_name, ability in self._abilities.items():
            if ability.user_override:
                self._abilities[ability_name] = ability.user_override
                continue
            for item in self._items:
                pass
                # setters: List[ScoreSetter] = [component for component in item.components.values()
                #                               if type(component) == ScoreSetter and component.ability == ability_name]
                # if setters:
                #     ability.score = max([setter.score for setter in setters])
                # elif ScoreMaxSetter in component_types:
                #     'set ability max'
                # elif ScoreChanger in component_types:
                #     'change score'


class Ability(object):
    def __init__(self, *, name=None, base=0):
        self.max = 20
        self.score = None
        self.user_override = None
        self.base = base
        self.name = name
