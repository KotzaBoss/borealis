import abc
from abc import ABC, abstractmethod
from typing import Any


class Component(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def update(self, char_sheet: dict) -> Any: ...


class Bollean:
    def __init__(self, *, bvalue: bool = ...) -> None: ...

    @property
    def bvalue(self): ...

    @bvalue.setter
    def bvalue(self, bvalue: Any) -> None: ...

    def __bool__(self): ...
