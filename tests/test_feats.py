from pprint import pprint

from character import Character
from feats import Actor, Alert, Athlete, DefensiveDuelist


def test_feats():
    ch = Character(feats=[
        Actor(),
        Alert(),
        Athlete(),
        DefensiveDuelist()
    ])
    print()
    pprint(ch.feats)
