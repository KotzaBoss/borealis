from character import Character
from components.score_manipulator import Changer
from item import Item
from utils.resources import Initiative


def test_experimental():
    print()
    i = Item(Changer(score=1, resource=Initiative), name='Paktol')
    c = Character(items=[i])
    print(c)
    c.delete_item(i)
    print(c)
