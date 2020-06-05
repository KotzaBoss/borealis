from typing import Any, List, Union

from item import Item
from item.components import Bollean, Component


class Container(Component, Bollean):
    def __init__(self, stuff: Union[List[Item], Item] = ...) -> None: ...

    def __getitem__(self, item: Any): ...

    @property
    def container(self): ...

    def add(self, new_item: Union[List[Item], Item]) -> Any: ...

    def update(self, char_sheet: dict) -> Any: ...
