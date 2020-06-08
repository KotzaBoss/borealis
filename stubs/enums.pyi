from enum import Enum


class WEAPONTYPE(Enum): ...


class SKILL(Enum):
    ACROBATICS: str = ...
    ANIMAL_HANDLING: str = ...
    ARCANA: str = ...
    ATHLETICS: str = ...
    DECEPTION: str = ...
    ENDURANCE: str = ...
    HISTORY: str = ...
    INSIGHT: str = ...
    INTIMIDATION: str = ...
    INVESTIGATION: str = ...
    MEDICINE: str = ...
    NATURE: str = ...
    PERCEPTION: str = ...
    PERFORMANCE: str = ...
    PERSUASION: str = ...
    RELIGION: str = ...
    SLEIGHT_OF_HAND: str = ...
    STEALTH: str = ...
    STREETWISE: str = ...
    SURVIVAL: str = ...
    NONE: str = ...


class CONDITION(Enum):
    BLINDED: str = ...
    CHARMED: str = ...
    DEAFENED: str = ...
    FRIGHTENED: str = ...
    GRAPPLED: str = ...
    INCAPACITATED: str = ...
    INVISIBLE: str = ...
    PARALYSED: str = ...
    PETRIFIED: str = ...
    POISONED: str = ...
    PRONE: str = ...
    RESTRAINED: str = ...
    STUNNED: str = ...
    UNCONSCIOUS: str = ...
    NONE: str = ...


class RARITY(Enum):
    MUNDANE: str = ...
    COMMON: str = ...
    UNCOMMON: str = ...
    RARE: str = ...
    VERY: str = ...
    LEGENDARY: str = ...
    NONE: str = ...

    def describe(self): ...


class DAMAGETYPE(Enum):
    SLASHING: str = ...
    PIERCING: str = ...
    BLUDGEONING: str = ...
    POISON: str = ...
    ACID: str = ...
    FIRE: str = ...
    COLD: str = ...
    RADIANT: str = ...
    NECROTIC: str = ...
    LIGHTNING: str = ...
    THUNDER: str = ...
    FORCE: str = ...
    PSYCHIC: str = ...
    MAGIC: str = ...
    NONE: str = ...


class COIN(Enum):
    PLATINUM: str = ...
    GOLD: str = ...
    ELECTRUM: str = ...
    SILVER: str = ...
    COPPER: str = ...
    NONE: str = ...


class ABILITY(Enum):
    STR: str = ...
    DEX: str = ...
    CON: str = ...
    WIS: str = ...
    INT: str = ...
    CHA: str = ...
    NONE: str = ...


class ARMORTYPE(Enum):
    HEAVY: str = ...
    MEDIUM: str = ...
    LIGHT: str = ...
    NONE: str = ...


class WEAPONPROPERTY(Enum):
    AMMUNITION: str = ...
    FINESSE: str = ...
    HEAVY: str = ...
    LIGHT: str = ...
    LOADING: str = ...
    RANGE: str = ...
    REACH: str = ...
    SPECIAL: str = ...
    THROWN: str = ...
    TWOHANDED: str = ...
    VERSITILE: str = ...
    NONE: str = ...