from item.components import Component
from utils.enums import RARITY


class Rarity(Component):
    def __init__(self, rarity: RARITY = None):
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
