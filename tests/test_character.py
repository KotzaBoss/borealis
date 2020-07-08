from character import Character
from components.proficiency import Proficiency
from components.weight import Weight
from feats import Actor, InspiringLeader
from item import Item
from utils.resources import Speed


def test_character():
    char = Character(
        name="TAKIS",
        feats=[Actor(), InspiringLeader()],
        items=[Item(Weight(60))],
        proficiencies=[Proficiency(Speed)]
    )

    print()
    print(char)
