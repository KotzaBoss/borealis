from pprint import pprint

import pytest

from components.score_manipulator import Changer
from item import Item
from overlord import *


@pytest.mark.parametrize(
    'expr', [
        '1d6',
        '1d20',
        '1d10',
    ]
)
def test_roll(expr):
    print()
    print(Azathoth.awaken('roll ' + expr))


def test_new():
    print()
    c = Azathoth.awaken('new')
    print(c)


def test_view():
    print()
    c = Azathoth.awaken('new',
                        items=[
                            Item(Changer(score=1, resource=ABILITY.STR))
                        ])
    pprint(Azathoth.awaken('view', c, ABILITY.STR))
    # pprint(Azathoth.awaken('view', c, Initiative))
    # pprint(Azathoth.awaken('view', c, AC))
    pprint(Azathoth.awaken('view', c, ABILITY))
