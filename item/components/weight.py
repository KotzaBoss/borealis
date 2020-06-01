from typing import Union

from . import Component


class Mass(int):
    def __init__(self, value: int = -1):
        super().__init__()
        self._value = value

    def __add__(self, other):
        return self._value + other._value

    def __sub__(self, other):
        return self._value - other._value

    def to_imperial(self):
        pass

    def to_metric(self):
        pass


class Pound(Mass):
    def __init__(self, value: int = -1):
        super().__init__(value)

    def to_metric(self):
        return 0.453 * self._value

    def __repr__(self):
        if self._value < 1:
            return f"{self._value} {self.__class__.__name__}"
        else:
            return f"{self._value} {self.__class__.__name__}s"


class Kilogram(Mass):
    def __init__(self, value: int = -1):
        super().__init__(value)

    def to_imperial(self):
        return self._value / 0.453

    def __repr__(self):
        if self._value < 1:
            return f"{self._value} {self.__class__.__name__}"
        else:
            return f"{self._value} {self.__class__.__name__}s"


class Weight(Component):
    def __init__(self, weight: Union[Pound, Kilogram, int] = -1):
        if type(weight) == int:  # isinstance wont work check Capacity class
            weight = Pound(weight)
        self._weight = weight

    def __add__(self, other):
        return self + other

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return str(self._weight)
