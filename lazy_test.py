from enums import *
from item import Item
from item.components.ac import AC
from item.components.armortype import ArmorType
from item.components.bonuses import ACBonus, DamageBonus
from item.components.capacity import Capacity, CubicMeter
from item.components.charges import Charges
from item.components.cost import Cost
from item.components.damagetype import Resistance
from item.components.dc import DC
from item.components.dice import DamageDice
from item.components.durations import Don, EffectDuration
from item.components.rarity import Rarity, RARITY
from item.components.requirement import AbilityRequirement
from item.components.weight import Weight

if __name__ == '__main__':
    item = Item()

    item.insert_component(
        AC(13, 10, 5, True),
        Weight(8),
        ArmorType(),
        DamageBonus(6),
        ACBonus(88),
        Rarity(RARITY.LEGENDARY),
        DC(score=17, ability=ABILITY.DEX),
        Don(2),
        EffectDuration(4),
        DamageDice('1d8'),
        AbilityRequirement(14, ABILITY.CHA),
        Cost(),
        Capacity(CubicMeter(100)),
        Resistance({DAMAGETYPE.BLUDGEONING, DAMAGETYPE.MAGIC, DAMAGETYPE.NECROTIC}),
        Charges(3)
    )
    print(item)
