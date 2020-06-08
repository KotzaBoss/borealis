from typing import Any

from utils.enums import WEAPONPROPERTY
from item.components import Component


class WeaponProperty(Component):
    def __init__(self, property_: WEAPONPROPERTY = ...) -> None: ...

    @property
    def property(self): ...

    @property.setter
    def property(self, property_: Any) -> None: ...

    def update(self, char_sheet: dict) -> Any: ...
