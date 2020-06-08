from functools import wraps
from typing import Callable, Any


def func_runner(extra=None, when='before'):
    def inner(func: Callable[[Any], Any]):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if extra and when == 'before':
                print(extra)
            ret = func(*args, **kwargs)
            if extra and when == 'after':
                print(extra)
            return ret

        return wrapper

    return inner
