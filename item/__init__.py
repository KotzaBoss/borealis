from typing import Union, Set, List

from item.components import Component


class Item(object):
    """ Basic class for any item (weapon, armor, ring, ...) acquired by the player. """

    def __init__(self, name='Unamed Item', *, components: Union[Set[Component], List[Component]] = None):
        if not components:
            self._components = {}
        else:
            self._components = {}
            for component in components:
                self._components[component.__class__.__name__] = component
        self._name = name

    def insert_component(self, *component):
        for comp in component:
            if comp.__class__.__name__ in self._components.keys():
                raise KeyError(f"{comp.__class__.__name__} already a component of item: {self._name}.")
            self.components[comp.__class__.__name__] = comp

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def components(self):
        return self._components

    @components.setter
    def components(self, components):
        self._components = components

    def __repr__(self):
        return f"{self._name}\n" + ''.join(
            [f"{comp_name.ljust(25, '.')} : {comp_obj}\n" for comp_name, comp_obj in self.components.items()])