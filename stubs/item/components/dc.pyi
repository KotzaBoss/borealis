from typing import Any

from components import Component
from utils.enums import ABILITY as ABILITY


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

    def update(self, char_sheet: Character) -> Any: ...
