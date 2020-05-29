from abc import ABC, abstractmethod


class Component(ABC):
    """ Basic component class for any items. """

    @abstractmethod
    def update(self, char_sheet: dict):
        """ Any subclass must overide the update function. """
        pass
