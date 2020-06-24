import pytest

from components.proficiency import Proficiency


@pytest.mark.parametrize(
    'ability', [
        123,
        'ability1',
        None
    ]
)
def test_prof(ability):
    with pytest.raises(TypeError):
        p = Proficiency(ability)
