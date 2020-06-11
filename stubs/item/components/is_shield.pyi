from typing import Any

from item.components import Boolean, Component


class IsShield(Component, Boolean):
    def __init__(self, bvalue: bool = ...) -> None: ...

    def update(self, char_sheet: dict) -> Any: ...
