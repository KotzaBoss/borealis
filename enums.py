from enum import Enum


class COIN(Enum):
    PLATINUM = 'P'
    GOLD = 'G'
    ELECTRUM = 'E'
    SILVER = 'S'
    COPPER = 'C'


class ABILITY(Enum):
    STR = 'STR'
    DEX = 'DEX'
    CON = 'CON'
    WIS = 'WIS'
    INT = 'INT'
    CHA = 'CHA'


class ARMORTYPE(Enum):
    HEAVY = 'H'
    MEDIUM = 'M'
    LIGHT = 'L'
    NONE = 'N'
