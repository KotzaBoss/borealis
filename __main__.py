import os
import sys

sys.path.append(os.path.abspath(__file__ + "/../../"))  # 9000 IQ move

CMDS = ['new', 'import', 'exit', 'roll']


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
    from components.score_manipulator import Setter
    from character import Character
    from character import Ability
    from utils.enums import ABILITY
    from item import Item
    from overseer import AbilityOverseer

    ch = Character(items=[
        Item(Setter(score=10, resource=Ability(name=ABILITY.STR)))
    ]
    )
    print(ch.abilities)
    AbilityOverseer.calculate_ability_scores(ch)
    print(ch.abilities)
