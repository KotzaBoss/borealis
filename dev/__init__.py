from functools import wraps
from warnings import warn


def deprecated(msg='~'):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            warn(msg, DeprecationWarning)
            func(*args, **kwargs)

        return wrapper

    return inner
