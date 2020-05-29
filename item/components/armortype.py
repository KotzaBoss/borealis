from enums import ARMORTYPE
from . import Component


class ArmorType(Component):
    def __init__(self, arm_type: ARMORTYPE = ARMORTYPE.NONE):
        self._arm_type: ARMORTYPE = arm_type

    @property
    def armor_type(self):
        return self._arm_type

    @armor_type.setter
    def armor_type(self, armtype: ARMORTYPE):
        self._arm_type = armtype

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return str(self._arm_type.name)
