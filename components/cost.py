from __future__ import annotations

from functools import total_ordering

from components import Component
from utils.enums import COIN


@total_ordering
class Cost(Component):
    """ Cost dictionary {'p': 1, 'g': 15, 'e': 5, 's': 0, 'c': 1} """
    kwcoins = {'platinum', 'gold', 'electrum', 'silver', 'copper'}

    # @validate_kwargs(kwcoins, {int})
    def __init__(self, **kwargs):
        if not all([isinstance(coin, int) for coin in kwargs.values()]):
            raise ValueError
        if not all([kwarg in self.kwcoins for kwarg in kwargs]):
            raise KeyError
        self._cost = {getattr(COIN, key.upper()): val for key, val in kwargs.items()}


    def __eq__(self, other):
        return sum([value for value in self._cost.values()]) == \
               sum([value] for value in other._cost.values())

    def __lt__(self, other):
        return sum([value for value in self._cost.values()]) < \
               sum([value] for value in other._cost.values())

    # @validate_param_types([COIN])
    def __getitem__(self, item: COIN):
        return self._cost[item]

    # @validate_param_types([COIN, int])
    def __setitem__(self, key: COIN, value: int):
        if key not in {coin for coin in COIN}:
            raise KeyError(f"{key} not a coin")
        self._cost[key] = value

    @property
    def cost(self):
        return self._cost

    def update(self, char: Character):
        pass
