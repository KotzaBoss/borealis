from __future__ import annotations

from abc import ABC, abstractmethod


class Component(ABC):
    """ Basic component class for any items. """

    @abstractmethod
    def update(self, char: Character):
        """ Any subclass must overide the update function. """
        pass

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
        s = f"{self.__class__.__name__}("
        for k, v in self.__dict__.items():
            s += f"{k}={v}, "
        s += "\b\b)"
        return s


class Boolean(ABC):
    """ Abstract class to ensure derived class has the `__bool__` method. """

    @abstractmethod
    def __bool__(self):
        pass
