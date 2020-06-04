from functools import wraps

from enums import ABILITY
from item.components import Component


def validate_input(func):
    """ Decorator for AC class setter functions.

        Raises
        ------
        TypeError
            If argument of wrapped function is not type(dict)
        KeyError
            if argument of wrapped function is not subset of AC.AC_KEYS
    """

    @wraps(func)
    def wrapper(self, arg=None):
        if not arg:
            arg = {}
        if not type(arg) == dict:
            raise TypeError(f"type: '{type(arg)}' is not legal argue for {type(dict)} AC>")
        elif not set(arg.keys()).issubset(AC.AC_KEYS):
            raise KeyError(f"{set(arg.keys()).difference(AC.AC_KEYS)} are not argid AC keys.")
        func(self, arg)

    return wrapper


class AC(Component):
    AC_KEYS = {'flat ac', 'dex cap', 'dex', 'use dex'}

    @validate_input
    def __init__(self, ac: dict = None):
        if not ac:
            ac = {'flat ac': 0, 'dex cap': 0, 'dex': 0, 'use dex': False}
        ac.update({'AC': 0})
        self._ac = ac
        self.update_ac()

    def __getitem__(self, item):
        return self._ac[item]

    def __setitem__(self, key, value):
        if key not in self.AC_KEYS:
            raise KeyError(f"{key} not valid AC key.")
        self._ac[key] = value

    def get(self, key, default=None):
        return self._ac.get(key, default)

    def update(self, char_sheet: dict):
        if ABILITY.DEX in char_sheet:
            self._ac['dex'] = char_sheet['DEX']
            self.update_ac()

    def update_ac(self):
        if self._ac['use dex']:
            self._ac['AC'] = self._ac['flat ac'] + min(self._ac['dex cap'], self._ac['dex'])
        else:
            self._ac['AC'] = self._ac['flat ac']

    @property
    def ac(self):
        return self._ac

    @validate_input  # type: ignore
    @ac.setter
    def ac(self, value: dict):
        self._ac.update(value)

    def __repr__(self):
        return ' '.join(
            [str(self._ac['AC']),
             str({key: val for key, val in self._ac.items() if key != 'AC'})
             ]
        )
