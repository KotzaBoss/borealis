from enum import Enum


class WEAPONTYPE(Enum):
    pass


class RARITY(Enum):
    MUNDANE = 'MUNDANE'
    COMMON = 'COMMON'
    UNCOMMON = 'UNCOMMON'
    RARE = 'RARE'
    VERY = 'VERY RARE'
    LEGENDARY = 'LEGENDARY'
    NONE = 'NONE'

class DAMAGETYPE(Enum):
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
    NONE = 'NONE'


class COIN(Enum):
    PLATINUM = 'P'
    GOLD = 'G'
    ELECTRUM = 'E'
    SILVER = 'S'
    COPPER = 'C'
    NONE = 'NONE'

class ABILITY(Enum):
    STR = 'STR'
    DEX = 'DEX'
    CON = 'CON'
    WIS = 'WIS'
    INT = 'INT'
    CHA = 'CHA'
    NONE = 'NONE'


class ARMORTYPE(Enum):
    HEAVY = 'H'
    MEDIUM = 'M'
    LIGHT = 'L'
    NONE = 'N'


class WEAPONPROPERTY(Enum):
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
    NONE = 'NONE'
