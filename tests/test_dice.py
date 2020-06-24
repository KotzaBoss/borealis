import re

import pytest

from components.dice import DamageDice


@pytest.mark.parametrize(
    'xdy', [
        15,
        '1 d8',
        None
    ]
)
def test_dice(xdy):
    with pytest.raises((TypeError, re.error)) as e:
        d = DamageDice(xdy)
