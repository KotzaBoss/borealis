import pytest

from item.components.charges import Charges


@pytest.mark.parametrize(
    'charge', [
        '10',
        None,
        1.6
    ]
)
def test_charges(charge):
    with pytest.raises(TypeError):
        ch = Charges(charge)
