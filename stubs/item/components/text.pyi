from typing import Any

from . import Component as Component


class Text(Component):
    def __init__(self, txt: str = ...) -> None: ...

    @property
    def text(self): ...

    @text.setter
    def text(self, string: str) -> Any: ...

    def update(self, char_sheet: dict) -> Any: ...
