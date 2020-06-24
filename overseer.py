from typing import List, Dict

from character import Ability
from character import Character
from item.components.score_manipulator import ScoreChanger, ScoreSetter, ScoreMaxSetter
from utils.enums import ABILITY


class Overseer(object):
    pass


class AbilityOverseer(Overseer):
    @classmethod
    def get_manipulators(cls, char: Character):
        score_setters: Dict[ABILITY, List[Ability]] = {ab: [] for ab in ABILITY}
        max_setters: Dict[ABILITY, List[Ability]] = {ab: [] for ab in ABILITY}
        score_changers: Dict[ABILITY, List[Ability]] = {ab: [] for ab in ABILITY}
        for ability in char.abilities:
            for item in char.items:
                for component in item.components.values():
                    if type(component) == ScoreSetter and component.ability == ability:
                        score_setters[ability].append(component)
                    elif type(component) == ScoreMaxSetter and component.ability == ability:
                        max_setters[ability].append(component)
                    elif type(component) == ScoreChanger and component.ability == ability:
                        score_changers[ability].append(component)
        return score_setters, max_setters, score_changers

    @classmethod
    def calculate_ability_scores(cls, char: Character):
        score_setters, max_setters, score_changers = cls.get_manipulators(char)
        for ability, ability_obj in char.abilities.items():
            if ability_obj.user_override:
                char.abilities[ability] = ability_obj.user_override
            elif score_setters[ability]:
                for setter in score_setters[ability]:
                    char.abilities[ability].score = setter.score
                    break  # TODO: for multiple same score manipulators what is the priority?
            elif max_setters[ability]:
                for max_setter in max_setters[ability]:
                    char.abilities[ability].max = max_setter.score
                    break
            elif score_changers[ability]:
                for changer in score_changers[ability]:
                    char.abilities[ability].score += changer.score
                    break


class Cthulhu(object):
    _overseers: List[Overseer] = [AbilityOverseer, ...]

    @classmethod
    def overseers(cls):
        return cls._overseers

##### SINGLETON TYPE OVERSEERS #####
# class Overseer(type):
#     """ tomerghelber/singleton-factory
#     What should an overseer be?
#     A singleton or should they just be used as collections of functions?
#
#     """
#     _instances: Dict[object, Dict[int, object]] = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = {}
#         new = super().__call__(*args, **kwargs)  # Why does it return sub-overseer?
#         key = hash(new)
#         if key not in cls._instances[cls]:
#             cls._instances[cls][key] = new  # type(cls) is Overseer yet the dict has sub-Overseer key
#         return cls._instances[cls][key]
#     def __hash__(self):
#         return hash(self.__class__.__name__)


# class AbilityOverseer(object, metaclass=Overseer):
#     def __init__(self, char: Character):
#         self._abilities = char.abilities
#         self._items = char.items
#
#     def get_manipulators(self):
#         score_setters: Dict[ABILITY, List[Ability]] = {ab: [] for ab in ABILITY}
#         max_setters: Dict[ABILITY, List[Ability]] = {ab: [] for ab in ABILITY}
#         score_changers: Dict[ABILITY, List[Ability]] = {ab: [] for ab in ABILITY}
#         for ability in self._abilities:
#             for item in self._items:
#                 for component in item.components.values():
#                     if type(component) == ScoreSetter and component.ability == ability:
#                         score_setters[ability].append(component)
#                     elif type(component) == ScoreMaxSetter and component.ability == ability:
#                         max_setters[ability].append(component)
#                     elif type(component) == ScoreChanger and component.ability == ability:
#                         score_changers[ability].append(component)
#         return score_setters, max_setters, score_changers
#
#     def calculate_ability_scores(self):
#         score_setters, max_setters, score_changers = self.get_manipulators()
#         for ability, ability_obj in self._abilities.items():
#             if ability_obj.user_override:
#                 self._abilities[ability] = ability_obj.user_override
#             elif score_setters[ability]:
#                 for setter in score_setters[ability]:
#                     self._abilities[ability].score = setter.score
#                     break  # TODO: for multiple same score manipulators what is the priority?
#             elif max_setters[ability]:
#                 for max_setter in max_setters[ability]:
#                     self._abilities[ability].max = max_setter.score
#                     break
#             elif score_changers[ability]:
#                 for changer in score_changers[ability]:
#                     self._abilities[ability].score += changer.score
#                     break

# class Cthulhu(object, metaclass=Overseer):
#     def __init__(self):
#        self._overseers: List[Overseer] = []  # Overseer metaclass ensures one instance but perhaps set()?
#     @property
#     def overseers(self):
#         return self._overseers
#     @overseers.setter
#     def overseers(self, new):
#         self._overseers.append(new)
