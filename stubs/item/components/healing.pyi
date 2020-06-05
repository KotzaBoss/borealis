from typing import Any

from item.components import Component


class Healing(Component):
    def __init__(self, heal_points: int = ...) -> None: ...

    @property
    def heal_points(self): ...

    @heal_points.setter
    def heal_points(self, heal_points: Any) -> None: ...

    def update(self, char_sheet: dict) -> Any: ...
