from typing import Any, Set

from enums import DAMAGETYPE as DAMAGETYPE
from item.components import Component


class DamageType(Component):
    def __init__(self, dmg_types: Set[DAMAGETYPE] = ...) -> None: ...

    @property
    def types(self): ...

    @types.setter
    def types(self, dmg_types: Set[DAMAGETYPE]) -> Any: ...

    def update(self, char_sheet: dict) -> Any: ...


class Resistance(DamageType):
    def __init__(self, dmg_types: Any) -> None: ...


class Vulnerability(DamageType):
    def __init__(self, dmg_types: Any) -> None: ...


class Immunity(DamageType):
    def __init__(self, dmg_types: Any) -> None: ...
