from os import path
from typing import List

from ability import Ability
from components import Component
from components import ComponentCollection
from components.advantages import Adv
from components.proficiency import Proficiency
from components.requirement import AbilityRequirement
from components.score_manipulator import Changer
from utils.enums import ABILITY, SKILL
from utils.resources import Initiative, AC, ARMORTYPE, Speed

FEATS = {
    'DungeonDelver', 'Durable', 'Grapplerr', 'GreatWeaponMaster', 'Healer', 'HeavilyArmored', 'HeavyArmorMaster',
    'InspiringLeader', 'KeenMind', 'LightlyArmored', 'Linguist', 'Lucky', 'MageSlayer', 'MagicInitiate', 'MartialAdept',
    'MediumArmorMaster', 'Mobile', 'ModeratelyArmored', 'MountedCombatant', 'Observant', 'PolearmMaster', 'Resilient',
    'RitualCaster', 'SavageAttacker', 'Sentinel', 'Sharpshooter', 'ShieldMaster', 'Skilled', 'Skulker', 'SpellSniper',
    'TavernBrawler', 'Tough', 'WarCaster', 'WeaponMaster'
}


class Feat(ComponentCollection):
    """ Base class for feats.

        FUTURE: Automate Instantiation by reading from database
    """

    def __init__(self, *components, prerequisite=None, **kwargs):
        self._prerequisite = prerequisite
        try:
            self._description = open(f"{path.dirname(__file__)}/descriptions/{self.__class__.__name__.lower()}.txt", 'r')
        except OSError:
            self._description = None
        super().__init__(*components, name=self.__class__.__name__)

    @property
    def description(self):
        return self._description.read() if self._description else 'No Description Availlable'

    @property
    def prerequisite(self):
        return self._prerequisite


class Actor(Feat):
    def __init__(self):
        super().__init__(
            Changer(score=1, resource=ABILITY.CHA),
            Adv(resource=SKILL.DECEPTION),
            Adv(resource=SKILL.PERFORMANCE),
        )


class Alert(Feat):
    def __init__(self):
        super().__init__(
            Changer(score=5, resource=Initiative),
        )


class Athlete(Feat):
    def __init__(self):
        super().__init__(
            *self.custom(),
        )

    def custom(self) -> List[Component]:
        while (uin := input('STR or DEX? ')) not in ['STR', 'DEX']:
            pass
        return [Changer(score=1, resource=ABILITY.__members__[uin])]


class Charger(Feat):
    def __init__(self):
        super().__init__()


class CrossbowExpert(Feat):
    def __init__(self):
        super().__init__()


class DefensiveDuelist(Feat):
    def __init__(self):
        super().__init__(
            prerequisite=AbilityRequirement(Ability(name=ABILITY.DEX, base=20)),
        )


class DualWielder(Feat):
    def __init__(self):
        super().__init__(
            Changer(score=1, resource=AC)
        )


class DungeonDelver(Feat):
    def __init__(self):
        super().__init__()


class Durable(Feat):
    def __init__(self):
        super().__init__(
            Changer(score=1, resource=ABILITY.CON)
        )


class ElementalAdept(Feat):
    def __init__(self):
        super().__init__()


class Grappler(Feat):
    def __init__(self):
        super().__init__(
            prerequisite=AbilityRequirement(Ability(name=ABILITY.STR, base=13))
        )


class GreatWeaponMaster(Feat):
    def __init__(self):
        super().__init__()


class Healer(Feat):
    def __init__(self):
        super().__init__()


class HeavilyArmored(Feat):
    def __init__(self):
        super().__init__(
            Changer(score=1, resource=ABILITY.STR),
            Proficiency(resource=ARMORTYPE.HEAVY),
            prerequisite=Proficiency(resource=ARMORTYPE.MEDIUM)
        )


class HeavyArmorMaster(Feat):
    def __init__(self):
        super().__init__(
            Changer(score=1, resource=ABILITY.STR),
            prerequisite=Proficiency(resource=ARMORTYPE.HEAVY)
        )


class InspiringLeader(Feat):
    def __init__(self):
        super().__init__(
            prerequisite=AbilityRequirement(Ability(name=ABILITY.CHA, base=13))
        )


class KeenMind(Feat):
    def __init__(self):
        super().__init__(
            Changer(score=1, resource=ABILITY.INT)
        )


class LightlyArmored(Feat):
    def __init__(self):
        super().__init__(
            *self.custom(),
            Proficiency(resource=ARMORTYPE.LIGHT)
        )

    def custom(self) -> List[Component]:
        while (uin := input('STR or DEX? ')) not in ['STR', 'DEX']:
            pass
        return [Changer(score=1, resource=ABILITY.__members__[uin])]


class Linguist(Feat):
    def __init__(self):
        super().__init__(
            Changer(score=1, resource=ABILITY.INT)
        )


class Lucky(Feat):
    def __init__(self):
        super().__init__()


class MageSlayer(Feat):
    def __init__(self):
        super().__init__()


class MagicInitiate(Feat):
    def __init__(self):
        super().__init__()


class MartialAdept(Feat):
    def __init__(self):
        super().__init__()


class MediumArmorMaster(Feat):
    def __init__(self):
        super().__init__(
            prerequisite=Proficiency(resource=ARMORTYPE.MEDIUM)
        )


class Mobile(Feat):
    def __init__(self):
        super().__init__(
            Changer(score=10, resource=Speed)
        )


class ModeratelyArmored(Feat):
    def __init__(self):
        super().__init__(
            *self.custom(),
            Proficiency(resource=ARMORTYPE.MEDIUM),
            Proficiency(resource=ARMORTYPE.SHIELD),
        )

    def custom(self) -> List[Component]:
        while (uin := input('STR or DEX? ')) not in ['STR', 'DEX']:
            pass
        return [Changer(score=1, resource=ABILITY.__members__[uin])]


class MountedCombatant(Feat):
    def __init__(self):
        super().__init__()


class Observant(Feat):
    def __init__(self):
        super().__init__(
            *self.custom()
        )

    def custom(self) -> List[Component]:
        while (uin := input('INT or WIS? ')) not in ['INT', 'WIS']:
            pass
        return [Changer(score=1, resource=ABILITY.__members__[uin])]


class PolearmMaster(Feat):
    def __init__(self):
        super().__init__(
        )


class Resilient(Feat):
    def __init__(self):
        super().__init__(
            *self.custom()
        )

    def custom(self) -> List[Component]:
        while (uin := input(str(ABILITY.__members__.values()) + ' ?')) not in ABILITY.__members__.values():
            pass
        return [Changer(score=1, resource=ABILITY.__members__[uin])]


class RitualCaster(Feat):
    def __init__(self):
        super().__init__(
            prerequisite=AbilityRequirement(Ability(name=ABILITY.INT, base=13), Ability(name=ABILITY.WIS, base=13))
        )


class SavageAttacker(Feat):
    def __init__(self):
        super().__init__()


class Sentinel(Feat):
    def __init__(self):
        super().__init__()


class Sharpshooter(Feat):
    def __init__(self):
        super().__init__()


class ShieldMaster(Feat):
    def __init__(self):
        super().__init__()


class Skilled(Feat):
    def __init__(self):
        super().__init__()


class Skulker(Feat):
    def __init__(self):
        super().__init__(
            prerequisite=AbilityRequirement(Ability(name=ABILITY.DEX, base=13))
        )


class SpellSniper(Feat):
    def __init__(self):
        super().__init__()


class TavernBrawler(Feat):
    def __init__(self):
        super().__init__(
            *self.custom()
        )

    def custom(self) -> List[Component]:
        while (uin := input('STR, CON ?')) not in ['STR', 'CON']:
            pass
        return [Changer(score=1, resource=ABILITY.__members__[uin])]


class Tough(Feat):
    def __init__(self):
        super().__init__()


class WarCaster(Feat):
    def __init__(self):
        super().__init__()


class WeaponMaster(Feat):
    def __init__(self):
        super().__init__(
            *self.custom()
        )

    def custom(self) -> List[Component]:
        while (uin := input('STR, DEX ?')) not in ['STR', 'DEX']:
            pass
        return [Changer(score=1, resource=ABILITY.__members__[uin])]
