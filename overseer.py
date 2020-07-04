from abc import ABC, abstractmethod
from typing import List, Dict

from character import Character
from components.score_manipulator import Changer, Setter, MaxSetter, ScoreManipulator
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
        """ For each ability parse Component Collections and fill dictionaries for the 3
        categories of score manipulator
        """
        score_setters: Dict[ABILITY, List[ScoreManipulator]] = {ab: [] for ab in ABILITY}
        max_setters: Dict[ABILITY, List[ScoreManipulator]] = {ab: [] for ab in ABILITY}
        score_changers: Dict[ABILITY, List[ScoreManipulator]] = {ab: [] for ab in ABILITY}
        for ability in char.abilities:
            for item in char.items:
                for component in item.components:
                    if isinstance(component, Setter) and component.resource is ability:
                        score_setters[ability].append(component)
                    elif isinstance(component, MaxSetter) and component.resource is ability:
                        max_setters[ability].append(component)
                    elif isinstance(component, Changer) and component.resource is ability:
                        score_changers[ability].append(component)
        return score_setters, max_setters, score_changers

    @classmethod
    def calculate_ability_scores(cls, char: Character):
        """ For each type of ability score manipulaotor (ScoreManipulator with Ability resource),
        perform calculations
        """
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
