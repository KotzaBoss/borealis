from __future__ import annotations

from components import Component, Boolean
from item import Item


class Container(Component, Boolean):
    """ TODO: Figure out what/how to save items. What will the program look for? """

    def __init__(self, *stuff: Item):
        self._container = {item.name: item for item in stuff}
        super().__init__()

    def __getitem__(self, item):
        return self._container[item]

    def __bool__(self):
        return bool(self._container)

    @property
    def container(self):
        return self._container

    def add(self, *new_items: Item):
        self._container.update({item.name: item for item in new_items})

    def update(self, char: Character):
        pass
