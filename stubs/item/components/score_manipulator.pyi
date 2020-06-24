from typing import Any

from components import Component
from utils.enums import ABILITY as ABILITY


class ScoreManipulator(Component):
    def __init__(self, score: int = ..., ability: ABILITY = ...) -> None: ...

    @property
    def score(self): ...

    @score.setter
    def score(self, score: int) -> Any: ...

    @property
    def ability(self): ...

    @ability.setter
    def ability(self, ability: ABILITY) -> Any: ...

    def update(self, char_sheet: Character) -> Any: ...


class ScoreSetter(ScoreManipulator):
    def __init__(self, score: int = ..., ability: Any = ...) -> None: ...


class ScoreChanger(ScoreManipulator):
    def __init__(self, score: int = ..., ability: Any = ...) -> None: ...


class ScoreMaxSetter(ScoreManipulator):
    def __init__(self, score: int = ..., ability: Any = ...) -> None: ...
