from typing import Any

from enums import ABILITY
from item.components import Component


class Proficiency(Component):
    def __init__(self, ability: ABILITY = ...) -> None: ...

    @property
    def ability(self): ...

    @ability.setter
    def ability(self, ability: Any) -> None: ...

    def update(self, char_sheet: dict) -> Any: ...
