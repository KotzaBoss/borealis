from typing import Any

from components import Boolean, Component
from item import Item as Item


class Container(Component, Boolean):
    def __init__(self, *stuff: Item) -> None: ...

    def __getitem__(self, item: Any): ...

    @property
    def container(self): ...

    def add(self, *new_items: Item) -> Any: ...

    def update(self, char_sheet: Character) -> Any: ...
