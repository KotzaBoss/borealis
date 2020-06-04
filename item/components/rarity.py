from enums import RARITY
from item.components import Component


class Rarity(Component):
    def __init__(self, rarity: RARITY = RARITY.NONE):
        if type(rarity) != RARITY:
            raise TypeError(f"Expected {type(RARITY)}")
        self._rarity = rarity

    @property
    def rarity(self):
        return self._rarity

    @rarity.setter
    def rarity(self, rarity):
        self._rarity = rarity

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return str(self._rarity.name)
