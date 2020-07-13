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
