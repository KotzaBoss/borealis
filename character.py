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
        self.abilities: Dict[ABILITY, Ability] = \
            {ability: Ability(name=ability, base=init_rolls[i]) for i, ability in enumerate(ABILITY)}
        self.items = items if items else []


class AbilityOverseer(object):
    def __init__(self, char_sheet: Character):
        self._abilities = char_sheet.abilities
        self._items = char_sheet.items

    def get_manipulators(self, ability: ABILITY = None):
        score_setters: Dict[ABILITY, List[Ability]] = {ab: [] for ab in ABILITY}
        max_setters: Dict[ABILITY, List[Ability]] = {ab: [] for ab in ABILITY}
        score_changers: Dict[ABILITY, List[Ability]] = {ab: [] for ab in ABILITY}
        abilities = self._abilities.keys() if not ability else [ability]
        for ability in abilities:
            for item in self._items:
                for component in item.components.values():
                    if type(component) == ScoreSetter and component.ability == ability:
                        score_setters[ability].append(component)
                    elif type(component) == ScoreMaxSetter and component.ability == ability:
                        max_setters[ability].append(component)
                    elif type(component) == ScoreChanger and component.ability == ability:
                        score_changers[ability].append(component)
        return score_setters, max_setters, score_changers

    def calculate_ability_scores(self):
        score_setters, max_setters, score_changers = self.get_manipulators()
        for ability, obj in self._abilities.items():
            if obj.user_override:
                self._abilities[ability] = obj.user_override
            elif score_setters[ability]:
                for setter in score_setters[ability]:
                    self._abilities[ability].score = setter.score
                    break  # TODO: for multiple same score manipulators what is the priority?
            elif max_setters[ability]:
                for max_setter in max_setters[ability]:
                    self._abilities[ability].max = max_setter.score
                    break
            elif score_changers[ability]:
                for changer in score_changers[ability]:
                    self._abilities[ability].score += changer.score
                    break


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
