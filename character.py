from __future__ import annotations

from pprint import pformat
from typing import List, Dict, Tuple

from ability import Ability
from components.ac import AC
from components.proficiency import Proficiency
from components.requirement import AbilityRequirement
from components.score import Score
from utils.enums import ABILITY, SKILL
from utils.resources import Initiative, Speed, ProficiencyBonus, Inspiration
from utils.roll import roll_standard_table, DiceRoll


class Character(object):

    def __init__(self,
                 *,
                 init_rolls: List[int, int, int, int, int, int] = None,
                 items: List[ComponentCollection] = None,
                 feats: List[ComponentCollection] = None,
                 proficiencies: List[Proficiency] = None,
                 name: str = '-=>NONAME<=-'):

        self._name: str = name
        self._inspiration = Inspiration()
        self._proficiency_bonus: ProficiencyBonus = ProficiencyBonus()
        self._ac: AC = AC()
        self._initiative: Initiative = Initiative()
        self._speed: Speed = Speed()
        self._hp = {'max': Score(), 'temp': Score(), 'curr': Score()}
        self._hit_dice = DiceRoll()
        self._features = []
        self._proficiencies = proficiencies if proficiencies else []
        self._spells = []  # spell sheets?
        if not init_rolls:
            init_rolls = roll_standard_table()
        self._abilities: Dict[ABILITY, Ability] = \
            {ability: Ability(name=ability, base=init_rolls[i]) for i, ability in enumerate(ABILITY)}
        self._skills = {skill: Score() for skill in SKILL}
        self._saving_throws = {ability: Score() for ability in ABILITY}
        self._items = items if items else []
        self._feats, err = self.check_feat_req(feats) if feats else ([], [])
        if err:
            print(f"prerequisites not met for {err}")

    # def __eq__(self, other):
    #     return all([self._name == other._name, self._abilities == other._abilities, self._items == other._items])

    def __contains__(self, item: Proficiency):
        """ Check if item in attribute depending on type. """
        if isinstance(item, Prociciency):
            return item.resource in self._proficiencies

    def check_feat_req(self, feats) -> Tuple[List[Feat], List[Feat]]:
        """ Check feats to ensure requirements are met. Separate passed from failed feats. """
        err = []
        for i, feat in enumerate(feats):
            if feat.prerequisite and isinstance(feat.prerequisite, AbilityRequirement):
                for ability in feat.prerequisite.requirement:
                    if self._abilities[ability.name].score > ability.score:
                        break
                else:
                    err.append(feat)
        return [feat for feat in feats if feat not in err], err

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
        return self._proficiency_bonus

    @proficiency.setter
    def proficiency(self, val):
        self._proficiency_bonus = val

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
    def feats(self):
        return self._feats

    @feats.setter
    def feats(self, val):
        self._feats = val

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
        return pformat(self.__dict__)
