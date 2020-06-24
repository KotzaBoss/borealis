from typing import Any

from components import Component
from utils.enums import WEAPONPROPERTY as WEAPONPROPERTY


class WeaponProperty(Component):
    def __init__(self, property_: WEAPONPROPERTY = ...) -> None: ...

    @property
    def property(self): ...

    @property.setter
    def property(self, property_: Any) -> None: ...

    def update(self, char_sheet: Character) -> Any: ...
