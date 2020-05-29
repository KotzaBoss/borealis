from enums import ABILITY
from item.components import Component


class Proficiency(Component):
    def __init__(self, ability: ABILITY = ABILITY.NONE):
        self._ability = ability

    @property
    def ability(self):
        return self._ability

    @ability.setter
    def ability(self, ability):
        self._ability = ability

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return self._ability.name
