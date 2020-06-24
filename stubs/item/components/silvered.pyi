from typing import Any

from components import Boolean, Component


class Silvered(Component, Boolean):
    def __init__(self, bvalue: bool = ...) -> None: ...

    def update(self, char_sheet: Character) -> Any: ...
