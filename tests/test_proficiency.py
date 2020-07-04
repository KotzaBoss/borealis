import pytest

from ability import Ability
from components.proficiency import Proficiency
from utils.enums import ARMORTYPE, ABILITY, SAVINGTHROW


@pytest.mark.parametrize(
    'resource', [
        123,
        'ability1',
        None,
        Ability(name=ABILITY.WIS),
        ARMORTYPE.MEDIUM,
        SAVINGTHROW.STR,
    ]
)
def test_prof(resource):
    if not isinstance(resource, ARMORTYPE) and not isinstance(resource, SAVINGTHROW):
        with pytest.raises(TypeError):
            p = Proficiency(resource)
    else:
        p = Proficiency(resource)
