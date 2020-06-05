from typing import Any

from item.components import Component


class Bonus(Component):
    def __init__(self, bonus: int = ...) -> None: ...

    @property
    def bonus(self): ...

    @bonus.setter
    def bonus(self, bonus: Any) -> None: ...

    def update(self, char_sheet: dict) -> Any: ...


class ACBonus(Bonus):
    def __init__(self, bonus: int = ...) -> None: ...


class SavingThrowBonus(Bonus):
    def __init__(self, bonus: int = ...) -> None: ...


class SkillBonus(Bonus):
    def __init__(self, bonus: int = ...) -> None: ...


class InitiativeBonus(Bonus):
    def __init__(self, bonus: int = ...) -> None: ...


class SpeedBonus(Bonus):
    def __init__(self, bonus: int = ...) -> None: ...


class MaxHPBonus(Bonus):
    def __init__(self, bonus: int = ...) -> None: ...


class TempHPBonus(Bonus):
    def __init__(self, bonus: int = ...) -> None: ...


class AttackBonus(Bonus):
    def __init__(self, bonus: int = ...) -> None: ...


class DamageBonus(Bonus):
    def __init__(self, bonus: int = ...) -> None: ...


class SpellAttackBonus(Bonus):
    def __init__(self, bonus: int = ...) -> None: ...


class SpellSaveDCBonus(Bonus):
    def __init__(self, bonus: int = ...) -> None: ...


class DamageBonusViaAbilityModifier(Bonus):
    def __init__(self, bonus: Any = ...) -> None: ...
