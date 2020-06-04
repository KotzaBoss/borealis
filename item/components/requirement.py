from typing import Union, Dict

from enums import ABILITY
from item.components import Component, Bollean


class Requirement(Component, Bollean):
    def __init__(self, requirement: Union[Dict[str, Union[int, ABILITY]], bool], **kwargs):
        super().__init__(**kwargs)  # forward keyword arguments (used by Bollean class)
        self._requirement = requirement

    @property
    def requirement(self):
        return self._requirement

    @requirement.setter
    def requirement(self, requirement):
        self._requirement = requirement

    def update(self, char_sheet: dict):
        pass


class AbilityRequirement(Requirement):
    def __init__(self, *, value: int = -666, ability: ABILITY = ABILITY.NONE):
        if any([type(value) != int, type(ability) != ABILITY]):
            raise TypeError("Expected type int value, type ABILITY: ability")
        super().__init__({'value': value, 'ability': ability})

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return f"{self._requirement['ability'].name} > {self._requirement['value']}"


class Attunement(Requirement):
    def __init__(self, attunement: bool = False):
        super().__init__(requirement=attunement, bvalue=attunement)

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return str(self._requirement)
