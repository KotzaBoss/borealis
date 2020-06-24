import pytest

from components.rarity import Rarity


@pytest.mark.parametrize(
    'rarity', [
        # RARITY.LEGENDARY,
        'Legendary',
        10
    ]
)
def test_rarity(rarity):
    with pytest.raises(TypeError):
        r = Rarity(rarity)
