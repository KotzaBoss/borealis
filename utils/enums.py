from enum import Enum


class BaseEnum(Enum):
    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"


class WEAPONTYPE(BaseEnum):
    pass


class SKILL(BaseEnum):
    ACROBATICS = 'ACROBATICS'
    ANIMAL_HANDLING = 'ANIMAL_HANDLING'
    ARCANA = 'ARCANA'
    ATHLETICS = 'ATHLETICS'
    DECEPTION = 'DECEPTION'
    ENDURANCE = 'ENDURANCE'
    HISTORY = 'HISTORY'
    INSIGHT = 'INSIGHT'
    INTIMIDATION = 'INTIMIDATION'
    INVESTIGATION = 'INVESTIGATION'
    MEDICINE = 'MEDICINE'
    NATURE = 'NATURE'
    PERCEPTION = 'PERCEPTION'
    PERFORMANCE = 'PERFORMANCE'
    PERSUASION = 'PERSUASION'
    RELIGION = 'RELIGION'
    SLEIGHT_OF_HAND = 'SLEIGHT_OF_HAND'
    STEALTH = 'STEALTH'
    STREETWISE = 'STREETWISE'
    SURVIVAL = 'SURVIVAL'


class CONDITION(BaseEnum):
    BLINDED = 'BLINDED'
    CHARMED = 'CHARMED'
    DEAFENED = 'DEAFENED'
    FRIGHTENED = 'FRIGHTENED'
    GRAPPLED = 'GRAPPLED'
    INCAPACITATED = 'INCAPACITATED'
    INVISIBLE = 'INVISIBLE'
    PARALYSED = 'PARALYSED'
    PETRIFIED = 'PETRIFIED'
    POISONED = 'POISONED'
    PRONE = 'PRONE'
    RESTRAINED = 'RESTRAINED'
    STUNNED = 'STUNNED'
    UNCONSCIOUS = 'UNCONSCIOUS'


class RARITY(BaseEnum):
    MUNDANE = 'MUNDANE'
    COMMON = 'COMMON'
    UNCOMMON = 'UNCOMMON'
    RARE = 'RARE'
    VERY = 'VERY RARE'
    LEGENDARY = 'LEGENDARY'

    # FUTURE: Can add methods for user references
    def describe(self):
        return f"Description of {self.name}"


class DAMAGETYPE(BaseEnum):
    SLASHING = 'SLASHING'
    PIERCING = 'PIERCING'
    BLUDGEONING = 'BLUDGEONING'
    POISON = 'POISON'
    ACID = 'ACID'
    FIRE = 'FIRE'
    COLD = 'COLD'
    RADIANT = 'RADIANT'
    NECROTIC = 'NECROTIC'
    LIGHTNING = 'LIGHTNING'
    THUNDER = 'THUNDER'
    FORCE = 'FORCE'
    PSYCHIC = 'PSYCHIC'
    MAGIC = 'MAGIC'


class COIN(BaseEnum):
    PLATINUM = 'P'
    GOLD = 'G'
    ELECTRUM = 'E'
    SILVER = 'S'
    COPPER = 'C'


class ABILITY(BaseEnum):
    STR = 'STR'
    DEX = 'DEX'
    CON = 'CON'
    WIS = 'WIS'
    INT = 'INT'
    CHA = 'CHA'


class SAVINGTHROW(BaseEnum):
    """ Code duplication because enum attributes are bound to their class.

    >>> class base(Enum):
    ...     pass
    >>> class ability(base):
    ...     STR = 'STR'
    >>> class saving(ability, Enum):  # only legal subclass
    ...     pass
    >>> type(saving.STR)
    <enum 'ability'>

    """
    STR = 'STR'
    DEX = 'DEX'
    CON = 'CON'
    WIS = 'WIS'
    INT = 'INT'
    CHA = 'CHA'

class ARMORTYPE(BaseEnum):
    HEAVY = 'H'
    MEDIUM = 'M'
    LIGHT = 'L'
    SHIELD = 'S'

class WEAPONPROPERTY(BaseEnum):
    AMMUNITION = 'AMMUNITION'
    FINESSE = 'FINESSE'
    HEAVY = 'HEAVY'
    LIGHT = 'LIGHT'
    LOADING = 'LOADING'
    RANGE = 'RANGE'
    REACH = 'REACH'
    SPECIAL = 'SPECIAL'
    THROWN = 'THROWN'
    TWOHANDED = 'TWOHANDED'
    VERSITILE = 'VERSITILE'
