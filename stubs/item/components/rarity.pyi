from typing import Any

from enums import RARITY
from item.components import Component


class Rarity(Component):
    def __init__(self, rarity: RARITY = ...) -> None: ...

    @property
    def rarity(self): ...

    @rarity.setter
    def rarity(self, rarity: Any) -> None: ...

    def update(self, char_sheet: dict) -> Any: ...
