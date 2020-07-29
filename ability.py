from __future__ import annotations

from functools import total_ordering
from typing import Union


@total_ordering
class Ability(object):
    def __init__(self, *, name: ABILITY = None, base=0):
        self._max = 20
        self._score = base
        self._name = name
        # self.base = base
        # self.user_override = None

    def __add__(self, other):
        return self._score + other

    def __radd__(self, other):
        return self._score + other

    def __eq__(self, other: Union[Ability, int]):
        if isinstance(other, self.__class__):
            return self._score == other._score
        else:
            return self._score == other

    def __lt__(self, other: Union[Ability, int]):
        if isinstance(other, self.__class__):
            return self._score < other._score
        else:
            return self._score < other

    def get_modifier(self):
        return (self._score - 10) // 2

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, val):
        self._max = val

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, val):
        self._score = val

    @property
    def name(self):
        return self._name

    def __repr__(self):
        s = f"{self.__class__.__name__}("
        for k, v in self.__dict__.items():
            s += f"{k}={v}, "
        s = s[:-2] + ')'
        return s
