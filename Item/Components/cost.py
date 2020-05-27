from enums import COIN
from .component import Component


class Cost(Component):
    """ Cost dictionary {'p': 1, 'g': 15, 'e': 5, 's': 0, 'c': 1} """

    def __init__(self, cost=None):
        if cost is None:
            cost = {COIN.PLATINUM: 0, COIN.GOLD: 0, COIN.ELECTRUM: 0, COIN.SILVER: 0, COIN.COPPER: 0}
        self._cost = cost

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost_dict):
        self._cost = cost_dict

    def __repr__(self):
        return str(self.cost)
