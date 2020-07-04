import pytest

from character import Ability
from components.requirement import AbilityRequirement, Attunement, ABILITY


@pytest.mark.parametrize(
    'ability', [
        'DEX',
        Ability(name=ABILITY.CHA, base=10),
    ]
)
def test_ability_req(ability):
    if not isinstance(ability, Ability):
        with pytest.raises(TypeError):
            ar = AbilityRequirement(ability)
    else:
        ar = AbilityRequirement(ability)


@pytest.mark.parametrize(
    'val, expected', [
        (0, False),
        (False, False),
        (True, True),
        (1, True),
        ('a', True),
    ]
)
def test_attun(val, expected):
    at = Attunement(val)
    assert bool(at.requirement) is expected
