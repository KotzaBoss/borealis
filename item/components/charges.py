from item.components import Component


class Charges(Component):
    def __init__(self, init_charge: int = -1):
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

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return str(self._charges)
