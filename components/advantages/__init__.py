"""
THOUGHT: Should __init__ arguments be a set/list or implement them with *args ?
"""
from __future__ import annotations

__all__ = ['Advantage', 'Disadvantage', 'OnAbilityCheck', 'OnAbilitySavingThrow',
           'OnConditionSavingThrow', 'OnSkill', 'OnAttack', 'OnDeathSavingThrow']

from typing import Union

from components import Component, Boolean
from utils.enums import ABILITY, CONDITION, SKILL


class _Advantage_Type(Boolean):
    def __init__(self, on: Union[ABILITY, CONDITION, SKILL, bool] = None, **kwargs):
        super().__init__(bvalue=bool(on))  # Enums give bool == True
        self._on = on

    def __repr__(self):
        return f"{self.__class__.__name__}(_on={self._on})"


class _Advantage_Component(Component):
    def __init__(self, *advantages: _Advantage_Type):
        self._advantage = {adv.__class__.__name__: adv for adv in advantages}  # type: ignore

    def update(self, char: Character):
        # if 'advantage_type' in char_sheet:
        #      self._advantage['advantage_type'] = char_sheet['advantage_type']
        pass


class Advantage(_Advantage_Component):
    def __init__(self, *advantages: _Advantage_Type):
        super().__init__(*advantages)

    @property
    def advantage(self):
        return super()._advantage


class Disadvantage(_Advantage_Component):
    def __init__(self, *disadvantages: _Advantage_Type):
        super().__init__(*disadvantages)

    @property
    def disadvantage(self):
        return super()._advantage


class OnAbilityCheck(_Advantage_Type):
    def __init__(self, ability: ABILITY = None):
        super().__init__(ability)


class OnAbilitySavingThrow(_Advantage_Type):
    def __init__(self, ability_saving_throw: ABILITY = None):
        super().__init__(ability_saving_throw)


class OnConditionSavingThrow(_Advantage_Type):
    def __init__(self, condition_saving_throw: CONDITION = None):
        super().__init__(condition_saving_throw)


class OnSkill(_Advantage_Type):  # CLARIFY: Change stealth to Skill Disadvantage with stealth skill enum (??) from gitlab
    def __init__(self, skill: SKILL = None):
        super().__init__(skill)


class OnAttack(_Advantage_Type):
    def __init__(self, bvalue: bool = False):
        super().__init__(on=bvalue, bvalue=bvalue)


class OnDeathSavingThrow(_Advantage_Type):
    def __init__(self, bvalue: bool = False):
        super().__init__(on=bvalue, bvalue=bvalue)
