from abc import ABC, abstractmethod


class Component(ABC):
    """ Basic component class for any items. """

    @abstractmethod
    def update(self, char_sheet: dict):
        """ Any subclass must overide the update function. """

class Bollean(object):
    """ Used for Components that are merely a bool value. 
        For multiple inheritance other superclasses should
        forward `bvalue` as a keyword argument so that it 
        is used to initialise this class.
    """

    def __init__(self, bvalue=True):
        self._bvalue = bvalue

    def __bool__(self):
        return self._bvalue
