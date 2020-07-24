from character import Character
from components.score_manipulator import Changer
from item import Item
from utils.resources import Initiative


def test_experimental():
    print()
    i = Item(Changer(score=1, resource=Initiative), name='Paktol')
    j = Item(Changer(score=2, resource=Initiative), name='Swagtastic')
    c = Character(items=[i, j], init_rolls=[10 for _ in range(6)])
    print('PRE DELETE', c, '\n')
    assert i in c.items and j in c.items
    c.delete_item(i)
    assert i not in c.items
    print('\nAFTER DELETE', c, '\n')


from overlord import Amun, StorageGod, Horus
from utils.resources import ABILITY

from components.score_manipulator import MaxSetter, Setter


def test_ability_score_mediator():
    print()
    Amun.awaken(
        items=[
            Item(
                Changer(score=1, resource=ABILITY.STR),
                Changer(score=1, resource=ABILITY.STR),
                MaxSetter(score=1, resource=ABILITY.STR),
                Setter(score=666, resource=ABILITY.STR)
            )
        ],
        init_rolls=[10 for _ in range(6)]
    )
    from pprint import pprint
    for char in StorageGod.characters:
        pprint(Horus.view(char, ABILITY))
#
