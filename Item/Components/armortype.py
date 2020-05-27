from enums import ARMORTYPE
from .component import Component


class ArmorType(Component):
    def __init__(self, arm_type: ARMORTYPE = ARMORTYPE.NONE):
        self._arm_type: ARMORTYPE = arm_type

    @property
    def armor_type(self):
        return self._arm_type

    @armor_type.setter
    def armor_type(self, armtype: ARMORTYPE):
        self._arm_type = armtype

    def __repr__(self):
        return str(self._arm_type.name)
