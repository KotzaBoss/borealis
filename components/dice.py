from __future__ import annotations

import re

from components import Component


class Dice(Component):
    """ TODO: Figure out better name for quantity of dice and type of die used """

    def __init__(self, die_expr: str = ''):
        if match := re.match(r'(\d+)d(\d+)', die_expr):
            self._dnum = match.group(1)
            self._dtype = match.group(2)
        else:
            raise re.error(f"no match for {die_expr}")

    @property
    def num(self):
        return self._dnum

    @num.setter
    def num(self, num):
        self._dnum = num

    @property
    def type(self):
        return self._dtype

    @type.setter
    def type(self, _type):
        self._dtype = _type

    def update(self, char: Character):
        pass


class DamageDice(Dice):
    def __init__(self, die_expr):
        super().__init__(die_expr)
