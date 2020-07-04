from __future__ import annotations

from typing import Union

from character import Ability
from components import Component, Boolean
from components.proficiency import Proficiency
from utils.enums import ABILITY


class Requirement(Component):
    """ Base class for requirements/prerequisites. """

    def __init__(self, requirement: Union[int, bool, ABILITY, Proficiency]):
        self._requirement = requirement
        super().__init__()

    @property
    def requirement(self):
        return self._requirement

    @requirement.setter
    def requirement(self, requirement):
        self._requirement = requirement

    def update(self, char: Character):
        pass


class AbilityRequirement(Requirement):
    """ TODO: What arguments for __init__"""

    def __init__(self, *abilities: Ability):
        if not all(isinstance(ability, Ability) for ability in abilities):
            raise TypeError
        super().__init__(abilities)

    def update(self, char: Character):
        pass

    def __repr__(self):
        s = f'{self.__class__.__name__}('
        for req in [f"{abil.name} > {abil.score}" for abil in self._requirement]:
            s += req + ' or '
        s += '\b\b\b\b)'
        return s


class ProficiencyRequirement(Requirement):
    def __init__(self, *proficiencies: Proficiency):
        super().__init__(proficiencies)

    def update(self, char: Character):
        pass

    # def __repr__(self):
    #     s = f'{self.__class__.__name__}('
    #     for req in [f"{prof.resource}prof.score}" for prof in self._requirement]:
    #         s += req + ' or '
    #     s += '\b\b\b\b)'
    #     return s


class Attunement(Requirement, Boolean):
    def __init__(self, attunement: bool = False):
        super().__init__(requirement=attunement)

    def __bool__(self):
        return bool(self.requirement)

    def update(self, char: Character):
        pass

    def __repr__(self):
        return str(self._requirement)
