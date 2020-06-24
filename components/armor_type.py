from __future__ import annotations
from __future__ import annotations

from components import Component
from utils.enums import ARMORTYPE


class ArmorType(Component):
    def __init__(self, arm_type: ARMORTYPE = None):
        self._arm_type: ARMORTYPE = arm_type

    @property
    def armor_type(self):
        return self._arm_type

    @armor_type.setter
    def armor_type(self, armtype: ARMORTYPE):
        self._arm_type = armtype

    def update(self, char: Character):
        pass
