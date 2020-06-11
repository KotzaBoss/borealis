from item.components import Component
from utils.enums import WEAPONPROPERTY


class WeaponProperty(Component):
    def __init__(self, property_: WEAPONPROPERTY = None):
        self._property = property_

    @property
    def property(self):
        return self._property

    @property.setter
    def property(self, property_):
        self._property = property_

    def update(self, char_sheet: dict):
        pass

