from typing import Any, List, Set, Union

from utils.enums import Enum


def validate_kwargs(keys: Union[Set[Any], Enum] = ..., value_types: Set[type] = ...) -> Any: ...


def validate_param_types(argtypes: List[type]) -> Any: ...
