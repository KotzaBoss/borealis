import pytest

from item.components.activated import Activated
from item.components.consumable import Consumable
from item.components.cursed import Cursed
from item.components.effect_on_command import EffectOnCommand
from item.components.is_shield import IsShield
from item.components.rechargable import Rechargeable
from item.components.silvered import Silvered

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
