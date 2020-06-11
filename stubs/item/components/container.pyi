from typing import Any

from item import Item as Item
from item.components import Boolean, Component


class Container(Component, Boolean):
    def __init__(self, *stuff: Item) -> None: ...

    def __getitem__(self, item: Any): ...

    @property
    def container(self): ...

    def add(self, *new_items: Item) -> Any: ...

    def update(self, char_sheet: dict) -> Any: ...
