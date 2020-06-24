import pytest

from components.activated import Activated
from components.consumable import Consumable
from components.cursed import Cursed
from components.effect_on_command import EffectOnCommand
from components.is_shield import IsShield
from components.rechargable import Rechargeable
from components.silvered import Silvered

boolleans = [Cursed, Activated, Consumable, EffectOnCommand,
             IsShield, Rechargeable, Silvered]


@pytest.mark.parametrize(
    'component, init, expected1, change, expected2',
    [(component, True, True, False, False) for component in boolleans]
)
def test_booleans(component, init, expected1, change, expected2):
    c = component(init)
    assert bool(c) is expected1
    c.bvalue = change
    assert bool(c) is expected2
