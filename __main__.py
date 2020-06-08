import sys

from character import Character

sys.path.append('/home/kotzaboss/Git')  # TODO:
from utils.roll import roll_3d6, roll_4d6_max3, roll_standard_table, roll_4d6_reroll1once_max3, roll_for_stats
from character import AbilityOverseer
from item import Item
from item.components.score_manipulator import ScoreMaxSetter, ScoreChanger
from utils.enums import ABILITY

CMDS = ['new', 'import', 'exit']
INIT_ROLLS = {'std': roll_standard_table,
              'pointbuy': None,
              '3d6': roll_3d6,
              '4d6max3': roll_4d6_max3,
              '4d6reroll1': roll_4d6_reroll1once_max3,
              'custom': None}


def get_input(*, expected=None, errmsg='', prompt=None):
    """ Automates getting input from user.
        Print prompt, get input, check it is in expected
        if not print errmsg
    """
    if prompt:
        print(prompt)
    if not expected:
        return input('>>> ')
    while True:
        if (user := input('>>> ')) not in expected:
            print(f"{user}: {errmsg}")
            continue
        return user


if __name__ == '__main__':
    c = AbilityOverseer(Character(items=[
        Item(ScoreMaxSetter(ability=ABILITY.DEX, score=123)),
        Item(ScoreMaxSetter(ability=ABILITY.DEX, score=1)),
        Item(ScoreChanger(ability=ABILITY.DEX, score=90))
    ]
    )
    )
    for i in c.get_manipulators():
        print(i)

    while True:
        user = get_input(expected=CMDS, errmsg='Unavailable command', prompt=CMDS)
        if user == 'exit':
            break
        if user == 'new':
            user = get_input(expected=INIT_ROLLS.keys(), errmsg='Unavailable roll type', prompt=INIT_ROLLS.keys())
            rolls = roll_for_stats(INIT_ROLLS[user])
