from __future__ import annotations

from components import Component
from utils.enums import ABILITY


class Proficiency(Component):
    def __init__(self, ability: ABILITY = None):
        if type(ability) != ABILITY:
            raise TypeError("Ability must be type ABILITY.")
        self._ability = ability

    @property
    def ability(self):
        return self._ability

    @ability.setter
    def ability(self, ability):
        self._ability = ability

    def update(self, char: Character):
        pass
