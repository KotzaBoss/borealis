""" Module containing all item components providing Bonuses

Taking note from the python.collections all bonuses are defined in the __init__.py module
simplifying the import command

from:
    from item.components.bonuses.specific_bonus_module import SpecificBonus
to:
    from item.components.bonuses import SpecificBonus
"""

__all__ = ['SkillBonus', 'InitiativeBonus', 'ACBonus', 'SavingThrowBonus',
           'SkillBonus', 'SpeedBonus', 'MaxHPBonus', 'TempHPBonus',
           'AttackBonus', 'DamageBonus', 'SpellAttackBonus', 'SpellSaveDCBonus']

from typing import Union

from item.components import Component
from utils.enums import ABILITY


class Bonus(Component):
    def __init__(self, bonus=-666):
        self._bonus: Union[int, ABILITY] = bonus

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, bonus):
        self._bonus = bonus

    def update(self, char_sheet: dict):
        if isinstance(self._bonus, ABILITY):
            pass
        else:
            pass


class ACBonus(Bonus):
    def __init__(self, bonus=-666):
        super().__init__(bonus)


class SavingThrowBonus(Bonus):
    def __init__(self, bonus=-666):
        super().__init__(bonus)


class SkillBonus(Bonus):
    def __init__(self, bonus=-666):
        super().__init__(bonus)


class InitiativeBonus(Bonus):
    def __init__(self, bonus=-666):
        super().__init__(bonus)


class SpeedBonus(Bonus):
    def __init__(self, bonus=-666):
        super().__init__(bonus)


class MaxHPBonus(Bonus):
    def __init__(self, bonus=-666):
        super().__init__(bonus)


class TempHPBonus(Bonus):
    def __init__(self, bonus=-666):
        super().__init__(bonus)


class AttackBonus(Bonus):
    def __init__(self, bonus=-666):
        super().__init__(bonus)


class DamageBonus(Bonus):
    def __init__(self, bonus=-666):
        super().__init__(bonus)


class SpellAttackBonus(Bonus):
    def __init__(self, bonus=-666):
        super().__init__(bonus)


class SpellSaveDCBonus(Bonus):
    def __init__(self, bonus=-666):
        super().__init__(bonus)


class DamageBonusViaAbilityModifier(Bonus):
    def __init__(self, bonus=None):
        super().__init__(bonus)
