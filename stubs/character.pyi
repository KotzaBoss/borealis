from typing import Any, List, Optional

from item import Item as Item
from utils.enums import ABILITY


class Character:
    name: Any = ...
    abilities: Any = ...
    items: Any = ...

    def __init__(self, *, init_rolls: Any = ..., items: List[Item] = ..., name: Any = ...) -> None: ...


class AbilityOverseer:
    def __init__(self, char_sheet: Character) -> None: ...

    def get_manipulators(self, ability: ABILITY = ...) -> Any: ...

    def calculate_ability_scores(self) -> None: ...


class Ability:
    max: int = ...
    score: Any = ...
    user_override: Any = ...
    base: Any = ...
    name: Any = ...

    def __init__(self, *, name: Optional[Any] = ..., base: int = ...) -> None: ...