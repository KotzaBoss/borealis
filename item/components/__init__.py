from abc import ABC, abstractmethod


class Component(ABC):
    """ Basic component class for any items. """

    @abstractmethod
    def update(self, char_sheet: dict):
        """ Any subclass must overide the update function. """


class Bollean(object):
    def __init__(self, bvalue):
        self._bvalue = bvalue

    def __bool__(self):
        return self._bvalue
