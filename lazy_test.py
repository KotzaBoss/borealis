from item import Item
from utils.enums import *
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
from item.components.cost import Cost
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
from utils.func_runner import func_runner
from utils.roll import roll

def item_creation_test(components, name='Unamed Item'):
    item = Item(name=name, components=components)
    print(item)
    return item


def roll_test(xdy=''):
    for _xdy in xdy:
        print(f"{_xdy} -> {roll(_xdy)}")


if __name__ == '__main__':
    item = item_creation_test(
        [
            AC(flat_ac=10, dex_cap=2, dex=5, use_dex=True),
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
            Cost(platinum=1, silver=6),
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
                    # Item(Cost(CoinDict(platinum=6, silver=3)))
                ]
            )
        ],
        name="Dragon's Vape"
    )

