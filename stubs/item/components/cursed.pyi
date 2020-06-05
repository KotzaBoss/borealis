from typing import Any

from item.components import Bollean, Component


class Cursed(Component, Bollean):
    def __init__(self, bvalue: bool = ...) -> None: ...

    def update(self, char_sheet: dict) -> Any: ...
