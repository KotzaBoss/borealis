from abc import ABC, abstractmethod
from typing import List, Dict

from character import Ability
from character import Character
from components.score_manipulator import ScoreChanger, ScoreSetter, ScoreMaxSetter
from utils.enums import ABILITY


class Overseer(ABC):
    """ Overseer Abstract Base Class. """

    @classmethod
    @abstractmethod
    def awaken(cls, *args, **kwargs):
        pass


class AbilityOverseer(Overseer):
    @classmethod
    def awaken(cls, char: Character):
        pass

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
