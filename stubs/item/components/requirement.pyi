from typing import Any, Dict, Union

from enums import ABILITY
from item.components import Bollean, Component


class Requirement(Component, Bollean):
    def __init__(self, requirement: Union[Dict[str, Union[int, ABILITY]], bool], **kwargs: Any) -> None: ...

    @property
    def requirement(self): ...

    @requirement.setter
    def requirement(self, requirement: Any) -> None: ...

    def update(self, char_sheet: dict) -> Any: ...


class AbilityRequirement(Requirement):
    def __init__(self, *, value: int = ..., ability: ABILITY = ...) -> None: ...

    def update(self, char_sheet: dict) -> Any: ...


class Attunement(Requirement):
    def __init__(self, attunement: bool = ...) -> None: ...

    def update(self, char_sheet: dict) -> Any: ...
