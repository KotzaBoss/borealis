from typing import Any

from item.components import Component


class Duration(Component):
    def __init__(self, duration: int = ...) -> None: ...

    @property
    def duration(self): ...

    @duration.setter
    def duration(self, value: Any) -> None: ...

    def update(self, char_sheet: dict) -> Any: ...


class Don(Duration):
    def __init__(self, duration: int = ...) -> None: ...


class Doff(Duration):
    def __init__(self, duration: int = ...) -> None: ...


class EffectDuration(Duration):
    def __init__(self, duration: int = ...) -> None: ...
