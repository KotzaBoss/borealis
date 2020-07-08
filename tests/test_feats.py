from pprint import pprint

from character import Character
from feats import *


def test_feats():
    ch = Character(
        init_rolls=[100 for _ in range(6)],
        feats=[
            Actor(),
            Alert(),
            Athlete(),
            Charger(),
            CrossbowExpert(),
            DefensiveDuelist(),
            DualWielder(),
            Durable(),
            ElementalAdept(),
            Grappler(),
            GreatWeaponMaster(),
            Healer(),
            HeavilyArmored(),
            HeavyArmorMaster(),
            InspiringLeader(),
            KeenMind(),
            LightlyArmored(),
        ])
    print()
    # pprint(ch)
    pprint(ch.feats)

    print(Charger().description)
