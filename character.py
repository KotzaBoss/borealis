from __future__ import annotations

from functools import total_ordering
from typing import List, Dict, Union

from components.proficiency import Proficiency
from utils.enums import ABILITY
from utils.roll import roll_standard_table


class Character(object):
    def __init__(self, *,
                 init_rolls=None,
                 items: List[ComponentCollection] = None,
                 feats: List[ComponentCollection] = None,
                 proficiencies: List[Proficiency] = None,
                 name: str = '-=>NONAME<=-'):
        self._name = name
        self._inspiration = 0
        self._proficiency = 0
        self._ac = 0
        self._initiative = 0
        self._speed = 0
        self._hp = {}
        self._hit_dice = 0
        self._features = {}
        self._feats = feats
        self._proficiencies = proficiencies
        self._spells = {}  # spell sheets?
        if not init_rolls:
            init_rolls = roll_standard_table()
        self._abilities: Dict[ABILITY, Ability] = \
            {ability: Ability(name=ability, base=init_rolls[i]) for i, ability in enumerate(ABILITY)}
        self._skills = {}
        self._items = items if items else []

    def __eq__(self, other):
        return all([self._name == other._name, self._abilities == other._abilities, self._items == other._items])

    def __contains__(self, item: Proficiency):
        """ Check if item in attribute depending on type. """
        if isinstance(item, Prociciency):
            return item.resource in self._proficiencies

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def inspiration(self):
        return self._inspiration

    @inspiration.setter
    def inspiration(self, val):
        self._inspiration = val

    @property
    def proficiency(self):
        return self._proficiency

    @proficiency.setter
    def proficiency(self, val):
        self._proficiency = val

    @property
    def ac(self):
        return self._ac

    @ac.setter
    def ac(self, val):
        self._ac = val

    @property
    def initiative(self):
        return self._initiative

    @initiative.setter
    def initiative(self, val):
        self._initiative = val

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, val):
        self._speed = val

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, val):
        self._hp = val

    @property
    def hit_dice(self):
        return self._hit_dice

    @hit_dice.setter
    def hit_dice(self, val):
        self._hit_dice = val

    @property
    def features(self):
        return self._features

    @features.setter
    def features(self, val):
        self._features = val

    @property
    def proficiencies(self):
        return self._proficiencies

    @proficiencies.setter
    def proficiencies(self, val):
        self._proficiencies = val

    @property
    def spells(self):
        return self._spells

    @spells.setter
    def spells(self, val):
        self._spells = val

    @property
    def abilities(self):
        return self._abilities

    @abilities.setter
    def abilities(self, val):
        self._abilities = val

    @property
    def skills(self):
        return self._skills

    @skills.setter
    def skills(self, val):
        self._skills = val

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, val):
        self._items = val

    def __repr__(self):
        return str(self.__dict__.items())
        # return f"{self._name}\n{self._abilities}\n{self._items}"


@total_ordering
class Ability(object):
    def __init__(self, *, name: ABILITY = None, base=0):
        self.max = 20
        self.score = base
        self.user_override = None
        self.base = base
        self.name = name

    def __eq__(self, other: Union[Ability, int]):
        if isinstance(other, Ability):
            return self.score == other.score
        else:
            return self.score == other
        # return all([self.base == other.base, self.max == other.max, self.user_override == other.user_override,
        #             self.score == other.score, self.name == other.name])

    def __lt__(self, other: Union[Ability, int]):
        if isinstance(other, Ability):
            return self.score < other.score
        else:
            return self.score < other

    def __repr__(self):
        s = f"{self.__class__.__name__}("
        for k, v in self.__dict__.items():
            s += f"{k}={v}, "
        s += "\b\b)"
        return s
