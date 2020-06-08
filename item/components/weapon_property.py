from utils.enums import WEAPONPROPERTY
from item.components import Component


class WeaponProperty(Component):
    def __init__(self, property_: WEAPONPROPERTY = WEAPONPROPERTY.NONE):
        self._property = property_

    @property
    def property(self):
        return self._property

    @property.setter
    def property(self, property_):
        self._property = property_

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return self.property.name
