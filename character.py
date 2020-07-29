from __future__ import annotations

from pprint import pformat
from typing import List, Tuple

from deprecated import deprecated

from ability import Ability
from components.ac import AC
from components.proficiency import Proficiency
from components.requirement import AbilityRequirement
from components.score import Score
from components.score_manipulator import ScoreManipulator
from utils.enums import ABILITY, SKILL
from utils.resources import Initiative, Speed, ProficiencyBonus, Inspiration
from utils.roll import DiceRoll


class CharacterAttribute(object):
    def __repr__(self):
        return f"{self.__class__.__name__}({super().__repr__()})"


class Dependancy(object):
    """ Items, Freats, etc have multiple objects that may manipulate a score.
        but instead of copying the entire object again and again we could add a dependancy
        and keep only the object that manipulates it.

        Example
        -------
        Item1 which has many effects and one that affects initiative +1.
        Then initiative only needs to know about the +1.
        So we create a dependacy passing the object that demands the +1.
        When Item1 is deleted then we can be directed by its effects (+1 to INITIATIVE)
        and delete the dependacies.

        Obviously an overloard/overseer will be doing the adding/changing/deleting.
    """

    def __init__(self, obj=None, src=None):
        self.obj = obj
        self.src = src

    def __add__(self, other):
        return self.obj + other

    def __radd__(self, other):
        return self.obj + other

    def __repr__(self):
        return f"Dependancy({self.obj} from {self.src})"


class Items(CharacterAttribute, list):
    def __init__(self, *args):
        super().__init__(args)


class SavingThrows(CharacterAttribute, dict):
    def __init__(self):
        super().__init__({ability: Score() for ability in ABILITY})


class Skills(CharacterAttribute, dict):
    def __init__(self):
        super().__init__({skill: Score() for skill in SKILL})


class Abilities(CharacterAttribute, dict):
    def __init__(self, init_rolls=None):
        if not init_rolls:
            init_rolls = [10 for _ in range(6)]
        super().__init__(
            {ability: Ability(name=ability, base=init_rolls[i])
             for i, ability in enumerate(ABILITY)
             })


class HP(CharacterAttribute, dict):
    def __init__(self):
        super().__init__({'max': Score(), 'temp': Score(), 'curr': Score()})


class Proficiencies(CharacterAttribute, list):
    def __init__(self, *args):
        super().__init__(args)

    def __repr__(self):
        return super().__repr__() + ' Not Implemented!'


class Spells(CharacterAttribute, list):
    def __init__(self, *args):
        super().__init__(args)

    def __repr__(self):
        return super().__repr__() + ' Not Implemented!'


class Features(CharacterAttribute, list):
    def __init__(self, *args):
        super().__init__(args)

    def __repr__(self):
        return super().__repr__() + ' Not Implemented!'


class Feats(CharacterAttribute, list):
    def __init__(self, *args):
        super().__init__(args)

    def __repr__(self):
        return super().__repr__() + ' Not Implemented!'


class Character(object):

    def __init__(self,
                 *,
                 init_rolls: List[int, int, int, int, int, int] = None,
                 items: List[ComponentCollection] = None,
                 feats: List[ComponentCollection] = None,
                 proficiencies: List[Proficiency] = None,
                 name: str = '-=>NONAME<=-'):

        init_rolls = init_rolls if init_rolls else [10 for _ in range(6)]
        self._name: str = name
        self._inspiration: Inspiration = Inspiration()
        self._proficiency_bonus: ProficiencyBonus = ProficiencyBonus()
        self._ac: AC = AC()
        self._speed: Speed = Speed()
        self._hp = HP()
        self._hit_dice: DiceRoll = DiceRoll()
        self._features: Features = Features()
        self._proficiencies: Proficiencies = Proficiencies(*proficiencies) if proficiencies else Proficiencies()
        self._spells: Spells = Spells()
        self._abilities: Abilities = Abilities(init_rolls)
        self._initiative: Initiative = Initiative(self._abilities[ABILITY.DEX].get_modifier())
        self._skills: Skills = Skills()
        self._saving_throws: SavingThrows = SavingThrows()
        self._items: Items = Items(*items) if items else Items()
        self._feats, err = self.check_feat_req(feats) if feats else (
        Feats(), [])  # TODO: Check deprecation decorator of cheac_feat_req
        if err:
            print(f"prerequisites not met for {err}")

    def __getitem__(self, key):
        """ Use self[key] instead of self.__dict__[key]

            If key is a resource then self._resource is looked up
            Examples
            --------
            >>> from components.score_manipulator import Changer
            >>> from utils.resources import Initiative
            >>> from item import Item
            >>> c = Character(items=[Item(Changer(score=1, resource=Initiative))])
            >>> c[Initiative] == c.__dict__['_' + Initiative.__name__.lower()]
            True

        """
        if isinstance(key, type):
            key = '_' + key.__name__.lower()
        return self.__dict__[key]

    @deprecated('Logic moved to AbilityOverseer for abilities. Pending deletion')
    def add_item(self, *new_items):
        for item in new_items:
            for comp in item.components:
                if isinstance(comp, ScoreManipulator):
                    self[comp.resource].append(Dependancy(obj=comp, src=item))

    @deprecated('Logic moved to AbilityOverseer for abilities. Pending deletion.')
    def delete_item(self, del_item):  # TODO: That is the idea for dependancies...
        """
        for deleted thing
        find dependacies on thing  (could be infered from the thing
        eg. item with changer to initiative directs you to look for dependacies in initiative)
        delete dependacies
        delete thing
        ...
        """
        for i, item in enumerate(self._items):
            if item == del_item:
                for comp in item.components:  # QUESTION: follow item to depenndancies
                    if isinstance(comp, ScoreManipulator):
                        attr = self[comp.resource]
                        if getattr(attr, '__contains__', None):
                            for obj in attr:
                                if isinstance(obj, Dependancy) and obj.src == del_item:
                                    attr.remove(obj)
                # for attr_key, attr_value in self.__dict__.items():  # QUESTION: look everywhere????
                #     if getattr(attr_value, '__contains__', None):  # TODO: fix AC
                #         for obj in attr_value:
                #             if isinstance(obj, Dependancy) and obj.src == del_item:
                #                 attr_value.remove(obj)
            self._items.remove(item)

    @deprecated('Feats, features, etc will be directed by Yannis (YAML files)')
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
        return Feats(*[feat for feat in feats if feat not in err]), err

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
