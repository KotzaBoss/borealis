import pytest

from overlord import *
from utils.resources import Initiative
from utils.roll import roll


# import sys
# import os
# sys.path.append('/../')
# sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../'))


@pytest.mark.parametrize(
    'expr', [
        '1d6',
        '1d20',
        '1d10',
    ]
)
def test_roll(expr):
    assert Azathoth.awaken('roll ' + expr) == roll(expr)


def test_new():
    print()
    c = Azathoth.awaken('new')
    print(c)


def test_view():
    print()
    c = Azathoth.awaken('new')
    # print(Azathoth.awaken('view', c, ABILITY.STR))
    print(Azathoth.awaken('view', c, Initiative))
