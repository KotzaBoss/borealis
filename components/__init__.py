from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict


class Component(ABC):
    """ Basic component class for any items. """

    @abstractmethod
    def update(self, char: Character):
        """ Any subclass must overide the update function. """

    def __repr__(self):
        s = f"{self.__class__.__name__}("
        for k, v in self.__dict__.items():
            s += f"{k}={v}, "
        s += "\b\b)"
        return s


class ComponentCollection(ABC):
    """ Astract Base Class for Items, Features, Spells, Feats, ... """

    def __init__(self, *components: Component, name: str = 'Unamed Item'):
        self._components: Dict[str, Component] = {component.__class__.__name__: component for component in components}
        self._name = name

    def insert_component(self, *components):
        for comp in components:
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


class Boolean(object):
    """ Class to be inherited when `__bool__()` is required.

        For multiple inheritance other superclasses should
        forward `bvalue` as a keyword argument so that it
        is used to initialise this class.

        Subclasses should remember to update `self.bvalue = bool(...)`
        if their encapsulated data is changed.
    """

    def __init__(self, *, bvalue: bool = True):
        self.bvalue: bool = bvalue

    def __bool__(self):
        return self.bvalue
