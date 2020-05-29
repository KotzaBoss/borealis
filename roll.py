import re
from random import randint


def roll(expr: str):
    if match := re.match(r'(\d+)d(\d+)', expr):
        return int(match.group(1)) * randint(1, int(match.group(2)))
    else:
        return 0
