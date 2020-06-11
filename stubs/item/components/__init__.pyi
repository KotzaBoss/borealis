import abc
from abc import ABC, abstractmethod
from typing import Any

class Component(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def update(self, char_sheet: dict) -> Any: ...

class Boolean:
    bvalue: Any = ...

    def __init__(self, *, bvalue: bool = ...) -> None: ...

    def __bool__(self): ...
