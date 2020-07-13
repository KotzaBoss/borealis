import pytest

from utils.roll import rollv2, DiceRoll


@pytest.mark.parametrize(
    'expr', [
        '1 d6',
        '1d 56',
        'ad3',
        '13'
    ]
)
def test_rolls(expr):
    print()
    print(rollv2(DiceRoll('2d10')))
    with pytest.raises(ValueError):
        rollv2(DiceRoll(expr))
