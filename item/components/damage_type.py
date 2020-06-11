from typing import Set

from item.components import Component
from utils.enums import DAMAGETYPE


class DamageType(Component):
    def __init__(self, *dmg_types):
        if not dmg_types:
            dmg_types = set()
        self._types = {dmg_type for dmg_type in dmg_types}

    @property
    def types(self):
        return self._types

    @types.setter
    def types(self, dmg_types: Set[DAMAGETYPE]):
        self._types = dmg_types

    def update(self, char_sheet: dict):
        pass


class Resistance(DamageType):
    def __init__(self, *dmg_types):
        super().__init__(*dmg_types)


class Vulnerability(DamageType):
    def __init__(self, *dmg_types):
        super().__init__(*dmg_types)


class Immunity(DamageType):
    def __init__(self, *dmg_types):
        super().__init__(*dmg_types)
