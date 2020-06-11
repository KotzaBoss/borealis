from abc import ABC, abstractmethod


class Component(ABC):
    """ Basic component class for any items. """

    @abstractmethod
    def update(self, char_sheet: dict):
        """ Any subclass must overide the update function. """

    def __repr__(self):
        s = f"{self.__class__.__name__}("
        for k, v in self.__dict__.items():
            s += f"{k}={v}, "
        s += "\b\b)"
        return s


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
