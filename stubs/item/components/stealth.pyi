from typing import Any

from . import Component as Component


class Stealth(Component):
    def __init__(self, stealth: bool = ...) -> None: ...
    @property
    def stealth(self): ...
    @stealth.setter
    def stealth(self, value: bool) -> Any: ...
    def update(self, char_sheet: dict) -> Any: ...
