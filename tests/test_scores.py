import pytest

from ability import Ability
from components.score import Score


class NoArithmetic(object):
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.val + other

    def __sub__(self, other):
        return self.val - other


@pytest.mark.parametrize(
    'mods, ok', [
        ([Ability(base=666)], True),
        ([Ability(base=10), Ability(base=15), Ability(base=20)], True),
        ([Ability(base=10), NoArithmetic(10)], False)
    ]
)
def test_scores(mods, ok):
    print()
    if ok:
        s = Score(*mods)
        print(s)
    else:
        with pytest.raises(AttributeError):
            s = Score(*mods)
