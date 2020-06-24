from __future__ import annotations

from components import Component


class Charges(Component):
    def __init__(self, init_charge: int = -1):
        if type(init_charge) != int:
            raise TypeError("Charges must be int.")
        self._charges = init_charge

    def __add__(self, other: int):
        return self._charges + other

    def __sub__(self, other: int):
        return self._charges - other

    @property
    def charges(self):
        return self._charges

    @charges.setter
    def charges(self, charges):
        self._charges = charges

    def update(self, char: Character):
        pass
