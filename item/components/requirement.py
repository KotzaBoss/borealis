from enums import ABILITY
from . import Component


class Requirement(Component):
    def __init__(self, value=-666, ability: ABILITY = ABILITY.NONE):
        self._value: int = value
        self._ability = ability

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def ability(self):
        return self._ability

    @ability.setter
    def ability(self, ability):
        self._ability = ability

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return f"Requires {self._ability.name} > {str(self._value)}"


class AbilityRequirement(Requirement):
    def __init__(self, value=-666, ability: ABILITY = ABILITY.NONE):
        super().__init__(value, ability)
