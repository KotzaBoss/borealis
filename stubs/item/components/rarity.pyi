from typing import Any

from components import Component
from utils.enums import RARITY


class Rarity(Component):
    def __init__(self, rarity: RARITY = ...) -> None: ...

    @property
    def rarity(self): ...

    @rarity.setter
    def rarity(self, rarity: Any) -> None: ...

    def update(self, char_sheet: Character) -> Any: ...
