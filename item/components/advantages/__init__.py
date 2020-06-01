"""
THOUGHT: Should __init__ arguments be a set/list or implement them with *args ?
"""

from typing import Union, List, Set

from enums import ABILITY, CONDITION, SKILL
from item.components import Component, Bollean


class _Advantage_Type(Bollean):
    def __init__(self, on: Union[ABILITY, CONDITION, SKILL, bool] = None, **kwargs):
        super().__init__(bvalue=bool(on))  # Enums give bool == True
        self._on = on

    def __repr__(self):
        if isinstance(self._on, bool):
            return str(self._on)
        return self._on.name


class _Advantage_Component_Base(Component):
    def __init__(self, _advantages: Union[Set[_Advantage_Type], List[_Advantage_Type], _Advantage_Type] = None):
        if not _advantages:
            _advantages = {}
        if not isinstance(_advantages, _Advantage_Type):
            self._advantage = {obj.__class__.__name__: obj for obj in _advantages}  # THOUGHT: perhaps lower() the class name?
        else:
            self._advantage = {_advantages.__class__.__name__: _advantages}

    def update(self, char_sheet: dict):
        # if 'advantage' in char_sheet:
        #      self._advantage['advantage'] = char_sheet['advantage']
        pass

    def __repr__(self):
        return str(self._advantage)


class Advantage(_Advantage_Component_Base):
    def __init__(self, advantages: Union[Set[_Advantage_Type], List[_Advantage_Type], _Advantage_Type] = None):
        if not advantages:
            advantages = {}
        super().__init__(advantages)

    @property
    def advantage(self):
        return self._advantage


class Disadvantage(_Advantage_Component_Base):
    def __init__(self, disadvantages: Union[List[_Advantage_Type], Set[_Advantage_Type], _Advantage_Type] = None):
        if not disadvantages:
            disadvantages = {}
        super().__init__(disadvantages)

    @property
    def disadvantage(self):
        return self._advantage


class OnAbilityCheck(_Advantage_Type):
    def __init__(self, ability: ABILITY = ABILITY.NONE):
        super().__init__(ability)


class OnAbilitySavingThrow(_Advantage_Type):
    def __init__(self, ability_saving_throw: ABILITY = ABILITY.NONE):
        super().__init__(ability_saving_throw)


class OnConditionSavingThrow(_Advantage_Type):
    def __init__(self, condition_saving_throw: CONDITION = CONDITION.NONE):
        super().__init__(condition_saving_throw)


class OnSkill(_Advantage_Type):  # CLARIFICATION: Change stealth to Skill Disadvantage with stealth skill enum (??) from gitlab
    def __init__(self, skill: SKILL = SKILL.NONE):
        super().__init__(skill)


class OnAttack(_Advantage_Type):
    def __init__(self, bvalue: bool = False):
        super().__init__(on=bvalue, bvalue=bvalue)


class OnDeathSavingThrow(_Advantage_Type):
    def __init__(self, bvalue: bool = False):
        super().__init__(on=bvalue, bvalue=bvalue)
