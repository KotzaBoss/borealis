import sys

from character import Character

sys.path.append('/home/kotzaboss/Git')  # TODO:

from utils.roll import roll_3d6, roll_4d6_max3, roll_standard_table, roll_4d6_reroll1once_max3
from character import AbilityOverseer
from item import Item
from item.components.score_manipulator import ScoreMaxSetter, ScoreChanger, ScoreSetter
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
    c = AbilityOverseer(
        (ch := Character(items=[
            Item(ScoreMaxSetter(ability=ABILITY.DEX, score=123)),
            Item(ScoreSetter(ability=ABILITY.STR, score=1)),
            Item(ScoreChanger(ability=ABILITY.INT, score=90))
        ])
         )
    )
    from pprint import pprint

    pprint(ch.abilities)
    c.calculate_ability_scores()
    pprint(ch.abilities)
    # while True:
    #     user = get_input(expected=CMDS, errmsg='Unavailable command', prompt=CMDS)
    #     if user == 'exit':
    #         break
    #     if user == 'new':
    #         user = get_input(expected=INIT_ROLLS.keys(), errmsg='Unavailable roll type', prompt=INIT_ROLLS.keys())
    #         rolls = roll_for_stats(INIT_ROLLS[user])
    #         print(rolls)
