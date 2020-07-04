import re
from random import randint, seed

from borealis import DEBUG  # TODO: Ensure this works

from utils.enums import ABILITY


def roll(expr: str):
    """ `expr` is expected to be:
        xdy with no spaces, x/y must be numbers other than 0 and d is the character 'd'
    """
    if DEBUG:
        seed(666)
    if match := re.match(r'(\d+)d(\d+)', expr):
        return sum(
            [randint(1, int(match.group(2))) for _ in range(int(match.group(1)))]
        )
    else:
        return 0


def roll_standard_table():
    return [15, 14, 13, 12, 10, 8]


def roll_d4():
    return randint(1, 4)


def roll_d6():
    return randint(1, 6)


def roll_d8():
    return randint(1, 8)


def roll_d10():
    return randint(1, 10)


def roll_d12():
    return randint(1, 12)


def roll_d20():
    return randint(1, 20)


def roll_d100():
    return randint(1, 100)


def roll_d10000():  # Wild Magik
    return randint(1, 10000)


def roll_4d6_max3():
    rolls = list()
    for i in range(0, 4):
        rolls.append(roll_d6())
    rolls.sort(reverse=True)
    rolls = rolls[0:3]
    return rolls, sum(rolls)


def roll_4d6_reroll1once_max3():
    rolls = list()
    for i in range(0, 4):
        d6roll = roll_d6()
        if d6roll == 1:
            d6roll = roll_d6()
        rolls.append(d6roll)
    rolls.sort(reverse=True)
    rolls = rolls[0:3]
    return rolls, sum(rolls)


def roll_3d6():
    rolls = [roll_d6() for _ in range(3)]
    return rolls, sum(rolls)


def roll_for_stats(roll_func=None):
    if roll_func == roll_standard_table:
        return roll_standard_table()
    return [roll_func()[1] for _ in range(len(ABILITY))]
