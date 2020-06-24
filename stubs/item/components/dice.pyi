from typing import Any

from components import Component


class Dice(Component):
    def __init__(self, die_expr: str = ...) -> None: ...

    @property
    def num(self): ...

    @num.setter
    def num(self, num: Any) -> None: ...

    @property
    def type(self): ...

    @type.setter
    def type(self, _type: Any) -> None: ...

    def update(self, char_sheet: Character) -> Any: ...

class DamageDice(Dice):
    def __init__(self, die_expr: Any) -> None: ...
