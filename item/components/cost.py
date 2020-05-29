from typing import Union

from enums import COIN
from . import Component


class Cost(Component):
    """ Cost dictionary {'p': 1, 'g': 15, 'e': 5, 's': 0, 'c': 1} """

    def __init__(self, cost=None):
        if cost is None:
            cost = {COIN.PLATINUM: 0, COIN.GOLD: 0, COIN.ELECTRUM: 0, COIN.SILVER: 0, COIN.COPPER: 0}
        self._cost = cost

    def __getitem__(self, item: Union[COIN, str]):
        return self._cost[item]

    def __setitem__(self, key, value):
        self._cost[key] = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost_dict):
        self._cost = cost_dict

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return str({coin_type.name: self._cost[coin_type] for coin_type in self._cost})
