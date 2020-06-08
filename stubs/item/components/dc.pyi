from typing import Any

from utils.enums import ABILITY
from item.components import Component


class DC(Component):
    def __init__(self, score: int = ..., ability: ABILITY = ...) -> None: ...

    @property
    def score(self): ...

    @score.setter
    def score(self, score: Any) -> None: ...

    @property
    def ability(self): ...

    @ability.setter
    def ability(self, ability: Any) -> None: ...

    def update(self, char_sheet: dict) -> Any: ...
