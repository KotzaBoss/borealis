from __future__ import annotations

from functools import total_ordering
from typing import Union


@total_ordering
class Ability(object):
    def __init__(self, *, name: ABILITY = None, base=0):
        self.max = 20
        self.score = base
        self.user_override = None
        self.base = base
        self.name = name

    def __add__(self, other):
        return self.score + other

    def __radd__(self, other):
        return self.score + other

    def __eq__(self, other: Union[Ability, int]):
        if isinstance(other, self.__class__):
            return self.score == other.score
        else:
            return self.score == other

    def __lt__(self, other: Union[Ability, int]):
        if isinstance(other, self.__class__):
            return self.score < other.score
        else:
            return self.score < other

    @staticmethod
    def get_modifier(score: int):
        return (score - 10) // 2

    def __repr__(self):
        s = f"{self.__class__.__name__}("
        for k, v in self.__dict__.items():
            s += f"{k}={v}, "
        s = s[:-2] + ')'
        return s
