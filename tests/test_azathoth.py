import pytest

from character import Character
from overlord import Azathoth
from utils.roll import roll


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
    assert Azathoth.awaken('new') == Character()
