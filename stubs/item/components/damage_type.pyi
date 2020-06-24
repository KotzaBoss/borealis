from typing import Any, Set

from components import Component
from utils.enums import DAMAGETYPE as DAMAGETYPE


class DamageType(Component):
    def __init__(self, *dmg_types: Any) -> None: ...

    @property
    def types(self): ...

    @types.setter
    def types(self, dmg_types: Set[DAMAGETYPE]) -> Any: ...

    def update(self, char_sheet: Character) -> Any: ...

class Resistance(DamageType):
    def __init__(self, *dmg_types: Any) -> None: ...

class Vulnerability(DamageType):
    def __init__(self, *dmg_types: Any) -> None: ...

class Immunity(DamageType):
    def __init__(self, *dmg_types: Any) -> None: ...
