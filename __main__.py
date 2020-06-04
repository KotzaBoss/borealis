import sys

sys.path.append('/home/kotzaboss/Git')  # TODO:

from enums import *
from item import Item
from item.components.ac import AC
from item.components.activated import Activated
from item.components.advantages import OnAbilityCheck, \
    OnAttack, \
    Advantage, \
    Disadvantage, \
    OnConditionSavingThrow, \
    OnSkill
from item.components.armor_type import ArmorType
from item.components.bonuses import ACBonus, DamageBonus
from item.components.capacity import Capacity, CubicMeter
from item.components.charges import Charges
from item.components.consumable import Consumable
from item.components.cost import Cost, CoinDict
from item.components.cursed import Cursed
from item.components.damage_type import Resistance
from item.components.dc import DC
from item.components.dice import DamageDice
from item.components.durations import Don, EffectDuration
from item.components.healing import Healing
from item.components.rarity import Rarity, RARITY
from item.components.requirement import AbilityRequirement
from item.components.requirement import Attunement
from item.components.silvered import Silvered
from item.components.weight import Weight
from item.components.container import Container
from lazy_test import item_creation_test
from func_runner import func_runner

item_creation_test(
    [
        AC({'flat ac': 10, 'dex cap': 2, 'dex': 5, 'use dex': True}),
        Weight(8),
        ArmorType(),
        DamageBonus(6),
        ACBonus(88),
        Rarity(RARITY.LEGENDARY),
        DC(score=17, ability=ABILITY.DEX),
        Don(2),
        EffectDuration(4),
        DamageDice('1d8'),
        AbilityRequirement(value=14, ability=ABILITY.CHA),
        Cost(),
        Capacity(CubicMeter(1)),
        Resistance({DAMAGETYPE.BLUDGEONING, DAMAGETYPE.MAGIC, DAMAGETYPE.NECROTIC}),
        Charges(3),
        Attunement(True),
        Consumable(True),
        Cursed(),
        Activated(),
        Silvered(True),
        Healing(123),
        Advantage(
            {
                OnAbilityCheck(ABILITY.DEX),
                OnAttack(True),
                OnConditionSavingThrow(CONDITION.CHARMED)
            }
        ),
        Disadvantage({OnSkill(SKILL.ARCANA)}),
        Container(
            [
                Item(name='tiem1'),
                Item(Cost(CoinDict(platinum=6, silver=3)))
            ]
        )
    ],
    name="Dragon's Vape"
)


@func_runner(extra='lol', when='after')
def foo(x):
    return x + 1

# roll_test(['1d20', '2d6', '1d100', '1d1', '1d 2', 'd2'])
