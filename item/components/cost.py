from enums import COIN
from . import Component


class CoinDict(dict):
    coin_names = {'platinum', 'gold', 'electrum', 'silver', 'copper'}

    def __init__(self, **kwargs):
        super().__init__()
        if not set(kwargs.keys()).issubset(self.coin_names):
            raise KeyError(f"Invalid coin names: {set(kwargs.keys()).difference(self.coin_names)}")
        elif not all(type(value) == int for value in kwargs.values()):
            raise ValueError("All coin types must have int value")
        else:
            self._coins = {COIN.PLATINUM: kwargs['platinum'], COIN.GOLD: kwargs['gold'],
                           COIN.ELECTRUM: kwargs['electrum'], COIN.SILVER: kwargs['silver'],
                           COIN.COPPER: kwargs['copper']}

    def __getitem__(self, item: COIN):
        return self._coins[item]

    def __setitem__(self, key: COIN, value: int):
        self._coins[key] = value

    def __repr__(self):
        return str(self._coins)


class Cost(Component):
    """ Cost dictionary {'p': 1, 'g': 15, 'e': 5, 's': 0, 'c': 1} """

    def __init__(self, cost: CoinDict = None):
        if cost is None:
            cost = CoinDict()
        self._cost = cost

    @property
    def cost(self):
        return self._cost

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return str({coin_type.name: self._cost[coin_type] for coin_type in self._cost})
