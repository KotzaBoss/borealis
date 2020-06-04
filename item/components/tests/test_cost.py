import pytest

from item.components.cost import Cost, CoinDict, COIN


@pytest.mark.parametrize(
    'p, g, e, s, c', [
        # (0, 0, 0, 0, 0),
        # (1, 2, 3, 4, 5),
        # (-1, -2, -3, -4, -5),
        ('a', 'b', 'c', 'd', 'e'),
        (COIN.PLATINUM, 1, 1, 1, 1)
    ]
)
def test_cost_values(p, g, e, s, c):
    with pytest.raises(ValueError):
        cost = Cost(CoinDict(platinum=p, gold=g, electrum=e, silver=s, copper=c))


@pytest.mark.parametrize(
    'p, g, e, s, c', [
        ('platinum', 'gold', 'electrum', 'silver', 'notcopper'),
        ('notplatinum', 'nnotgold', 'notelectrum', 'notsilver', 'notcopper')
    ]
)
def test_cost_keys(p, g, e, s, c):
    keys = {p: 0, g: 0, e: 0, s: 0, c: 0}
    with pytest.raises(KeyError):
        cost = Cost(CoinDict(**keys))
