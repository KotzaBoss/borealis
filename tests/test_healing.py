import pytest

from components.healing import Healing


@pytest.mark.parametrize(
    'hp', [
        'a',
        None
    ]
)
def test_heal(hp):
    with pytest.raises(TypeError):
        h = Healing(hp)
