import re
from random import randint, seed


def roll(expr: str, seed_=None):
    """ `expr` is expected to be:
        xdy with no spaces, x/y must be numbers other than 0 and d is the character 'd'
    """
    if seed_:
        seed(seed_)
    if match := re.match(r'(\d+)d(\d+)', expr):
        return sum(
            [randint(1, int(match.group(2))) for _ in range(int(match.group(1)))]
                   )
    else:
        return 0

def standard_table():
    return [15, 14, 13, 12, 10, 8]
