from typing import Union, Set, List, Dict

from item.components import Component


class Item(object):
    """ Basic class for any item (weapon, armor, ring, ...) acquired by the player. """

    def __init__(self, components: Union[Set[Component], List[Component], Component] = None, name: str = 'Unamed Item'):
        self._components: Dict[str, Component] = {}
        if components:
            if isinstance(components, Component):
                self._components[components.__class__.__name__] = components
            else:
                self._components = {component.__class__.__name__: component for component in components}
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
        return f"\n{self._name}\n" + \
              ''.join(
                   [f"{c_name.ljust(25, '.')} : {c_obj}\n" for c_name, c_obj in self._components.items()]
               )
