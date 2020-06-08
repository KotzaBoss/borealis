from typing import Any, List, Set, Union

from utils.enums import ABILITY, CONDITION, SKILL
from item.components import Bollean, Component


class _Advantage_Type(Bollean):
    def __init__(self, on: Union[ABILITY, CONDITION, SKILL, bool] = ..., **kwargs: Any) -> None: ...


class _Advantage_Component(Component):
    def __init__(self, _advantages: Union[Set[_Advantage_Type], List[_Advantage_Type], _Advantage_Type] = ...) -> None: ...

    def update(self, char_sheet: dict) -> Any: ...


class Advantage(_Advantage_Component):
    def __init__(self, advantages: Union[Set[_Advantage_Type], List[_Advantage_Type], _Advantage_Type] = ...) -> None: ...

    @property
    def advantage(self): ...


class Disadvantage(_Advantage_Component):
    def __init__(self, disadvantages: Union[List[_Advantage_Type], Set[_Advantage_Type], _Advantage_Type] = ...) -> None: ...

    @property
    def disadvantage(self): ...


class OnAbilityCheck(_Advantage_Type):
    def __init__(self, ability: ABILITY = ...) -> None: ...


class OnAbilitySavingThrow(_Advantage_Type):
    def __init__(self, ability_saving_throw: ABILITY = ...) -> None: ...


class OnConditionSavingThrow(_Advantage_Type):
    def __init__(self, condition_saving_throw: CONDITION = ...) -> None: ...


class OnSkill(_Advantage_Type):
    def __init__(self, skill: SKILL = ...) -> None: ...


class OnAttack(_Advantage_Type):
    def __init__(self, bvalue: bool = ...) -> None: ...


class OnDeathSavingThrow(_Advantage_Type):
    def __init__(self, bvalue: bool = ...) -> None: ...
