from functools import wraps
from typing import Set, Any, Callable, Optional, Union, List

from enums import Enum
from item.components import Component


def validate_kwargs(keys: Union[Set[Any], Enum] = None, value_types: Set[type] = None):
    """
    Wraps function that takes multiple kwargs as arguments.
    Validates key names and value types.
    If either argument is None then no validation occurs.

    Raises
    ------
    KeyError:
        If kwargs contain key not in `keys`
    TypeError:
        If kwargs contain value of type not in `value_types`


    >>> @validate_kwargs({'a', 'b', 'c'}, {int, str})
    ... def foo(*args, **kwargs):  # *args to catch self for methods
    ...     pass
    >>> foo(a=1, b='b', c=1.0)  # play around with different key names and value types

    """

    def inner(func: Callable[[Optional[Any], Any], Any]):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if keys:
                if type(keys) == Enum:
                    ks = {key for key in keys}
                else:
                    ks = keys
                if not (sub_keys := set(kwargs.keys())).issubset(ks):
                    raise KeyError(sub_keys.difference(ks))
            if value_types and not \
                    (sub_types := {type(value) for value in kwargs.values()}).issubset(value_types):
                raise TypeError(sub_types.difference(value_types))
            func(*args, **kwargs)

        return wrapper

    return inner


def validate_param_types(argtypes: List[type]):
    """
    Wraps function that takes multiple args as arguments.
    Validates argument value types in sequence.

    Raises
    ------
    TypeError:
        If argument doenst have correct pair type.

    >>> @validate_param_types([int, str])
    ... def foo(arg1, arg2):
    ...     pass
    >>> foo(1, 2)

    """

    def inner(func: Callable[[Optional[Any], Any], Any]):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg, arg_type in zip(args if not isinstance(args[0], Component) else args[1:],
                                     argtypes):
                if type(arg) != arg_type:
                    raise TypeError(f"{arg} is not expected type {arg_type}")
            func(*args, **kwargs)

        return wrapper

    return inner
