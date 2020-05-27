from enums import ABILITY
from .component import Component


class AC(Component):
    def __init__(self, flat_ac=-1, dex_cap=3, dex=3, use_dex=False):
        self._ac = flat_ac
        self._flat_ac = flat_ac
        self._use_dex = use_dex
        self._dex_cap = dex_cap
        self._dex = dex
        self.update_ac()

    def update(self, char_sheet: dict):
        if ABILITY.DEX in char_sheet:
            self._dex = char_sheet['DEX']
            self.update_ac()

    def update_ac(self):
        if self._use_dex:
            self._ac = self.flat_ac + min(self._dex_cap, self._dex)
        else:
            self._ac = self._flat_ac

    @property
    def flat_ac(self):
        return self._flat_ac

    @flat_ac.setter
    def flat_ac(self, value):
        self._flat_ac = value
        self.update_ac()

    @property
    def use_dex(self):
        return self._use_dex

    @use_dex.setter
    def use_dex(self, value):
        self._use_dex = value
        self.update_ac()

    @property
    def dex_cap(self):
        return self._dex_cap

    @dex_cap.setter
    def dex_cap(self, value):
        self._dex_cap = value
        self.update_ac()

    @property
    def dex(self):
        return self._dex

    @dex.setter
    def dex(self, value):
        self._dex = value
        self.update_ac()

    @property
    def ac(self):
        return self._ac

    @ac.setter
    def ac(self, value):
        self._ac = value

    def __repr__(self):
        return str(self._ac)
