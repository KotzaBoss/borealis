from typing import Union, List

from item import Item
from item.components import Component, Bollean


class Container(Component, Bollean):
    """ TODO: Figure out what/how to save items. What will the program look for? """

    def __init__(self, stuff: Union[List[Item], Item] = None):
        super().__init__(bvalue=bool(stuff))
        if not stuff:
            stuff = []  # type: ignore
        elif isinstance(stuff, Item):
            stuff = [stuff]
        self._container = {item.name: item for item in stuff}

    def __getitem__(self, item):
        return self._container[item]

    @property
    def container(self):
        return self._container

    def add(self, new_item: Union[List[Item], Item]):
        if isinstance(new_item, Item):
            new_item = [new_item]
        for item in new_item:
            self._container[item.name] = item

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return str(self._container)
