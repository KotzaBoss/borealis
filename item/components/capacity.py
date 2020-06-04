from typing import Union

from item.components import Component


class Volume(int):
    def __init__(self, value: int = -1):
        super().__init__()
        self._value = value

    def __add__(self, other):
        return self._value + other._value

    def __sub__(self, other):
        return self._value - other._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    def to_imperial(self):
        pass

    def to_metric(self):
        pass


class CubicFeet(Volume):
    def __init__(self, value: int = -1):
        super().__init__(value)

    def to_metric(self):
        return self._value * 0.0283

    def __repr__(self):
        if self._value < 1:
            return f"{self._value} {self.__class__.__name__}"
        else:
            return f"{self._value} {self.__class__.__name__}s"


class CubicMeter(Volume):
    def __init__(self, value: int = -1):
        super().__init__(value)

    def to_imperial(self):
        return self._value * 35.31

    def __repr__(self):
        if self._value <= 1:
            return f"{self._value} {self.__class__.__name__}"
        else:
            return f"{self._value} {self.__class__.__name__}s"


class Capacity(Component):
    def __init__(self, capacity: Union[CubicMeter, CubicFeet, int] = -1):
        if type(capacity) not in {CubicMeter, CubicFeet, int}:
            raise TypeError("Expected CubicMeter, CubicFeet, or int")
        if type(capacity) == int:  # isinstance wont help because volume subclasses int
            capacity = CubicFeet(capacity)
        self._capacity = capacity

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return str(self._capacity)
