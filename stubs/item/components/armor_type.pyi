from typing import Any

from utils.enums import ARMORTYPE
from . import Component as Component


class ArmorType(Component):
    def __init__(self, arm_type: ARMORTYPE = ...) -> None: ...

    @property
    def armor_type(self): ...

    @armor_type.setter
    def armor_type(self, armtype: ARMORTYPE) -> Any: ...

    def update(self, char_sheet: dict) -> Any: ...
