from item.components import Component
from utils import validate_kwargs, validate_param_types
from utils.enums import ABILITY


class AC(Component):
    AC_KEYS = {'flat_ac', 'dex_cap', 'dex', 'use_dex'}

    @validate_kwargs(AC_KEYS, {int, bool})
    def __init__(self, *, flat_ac: int = 0, dex_cap: int = 0, dex: int = 0, use_dex: bool = False):
        self._ac = {'flat ac': flat_ac, 'dex cap': dex_cap, 'dex': dex,
                    'use dex': use_dex, 'AC': 0}
        self.update_ac()

    @validate_param_types([str])
    def __getitem__(self, item: str):
        return self._ac[item]

    @validate_param_types([str, int])
    def __setitem__(self, key: str, value: int):
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

    @validate_kwargs(AC_KEYS, {int, bool})
    @ac.setter
    def ac(self, **kwargs):
        self._ac.update(**kwargs)

