from abc import ABC, abstractmethod
from typing import List, Dict, Type

from deprecated import deprecated

from ability import Ability
from character import Character, Dependancy
from components.score_manipulator import Changer, Setter, MaxSetter, ScoreManipulator
from utils.enums import ABILITY


class Overseer(ABC):
    """ Overseer Abstract Base Class. """

    @classmethod
    @abstractmethod
    def awaken(cls, *args, **kwargs):
        pass


class AbilityOverseer(Overseer):
    """ Based on mediator design pattern.
        Keeps the dependancies from any source that alter a characters abilities.

        One ability overseer is instantiated for each character.
    """

    def __init__(self, char: Character):
        self._overseen = char
        self._deps: Dict[ABILITY, Dict[Type[ScoreManipulator], List[Dependancy]]] = \
            {ability: {Setter: [], MaxSetter: [], Changer: []} for ability in ABILITY}

    @property
    def overseen(self):
        return self._overseen

    @property
    def deps(self):
        return self._deps

    def calc(self, ability: ABILITY):
        final: Ability = self.overseen.abilities[ability]
        if mxsetters := self._deps[ability][MaxSetter]:
            final.max = mxsetters[0].obj.score
        if setters := self._deps[ability][Setter]:
            final.score = setters[0].obj.score
        elif changers := self._deps[ability][Changer]:
            final.score += sum(changers)
        return final

    def add_dep(self, *new_obj):
        for item in new_obj:
            for comp in item.components:
                if isinstance(comp, ScoreManipulator):
                    self._deps[comp.resource][type(comp)].append(Dependancy(obj=comp, src=item))

    def del_dep(self, *old_obj):
        for item in old_obj:
            self._deps.pop(item)

    @classmethod
    def awaken(cls, char: Character):
        pass

    @classmethod
    @deprecated('Logic completely changed (Dependencies used)')
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
    @deprecated('Logic completely changed (Dependencies used)')
    def calculate_ability_scores(cls, char: Character):
        """ For each type of ability score manipulator (ScoreManipulator with Ability resource),
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

    def __repr__(self):
        return f"AbilityOverseer({self.overseen.name=}, {self._deps=})"
