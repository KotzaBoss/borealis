import pytest

from item.components.requirement import AbilityRequirement, Attunement, ABILITY


@pytest.mark.parametrize(
    'val, ability', [
        (0, 'DEX'),
        ('0', ABILITY.CHA)
    ]
)
def test_ability_req(val, ability):
    with pytest.raises(TypeError):
        ar = AbilityRequirement(value=val, ability=ability)


@pytest.mark.parametrize(
    'val', [
        0,
        False,
        True,
        1,
        'a',
    ]
)
def test_attun(val):
    at = Attunement(val)
    assert at.requirement == at.bvalue
