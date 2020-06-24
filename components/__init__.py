from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


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

    def __init__(self, *components: Component, name: str = 'Unamed ComponentCollection'):
        self._components: List[Component] = [component for component in components]
        self._name = name

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
                   [f"{comp.__class__.__name__.ljust(25, '.')} : {comp}\n" for comp in self._components]
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
