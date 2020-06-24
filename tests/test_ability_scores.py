from character import Character
from components.score_manipulator import AbilitySetter, AbilityChanger, AbilityMaxSetter
from item import Item
from overseer import AbilityOverseer
from utils.enums import ABILITY


def test_foo():
    ch = Character(  # for init_items=None stats have std roll
        items=[
            Item(AbilityChanger(ability=ABILITY.STR, score=3), name='Ring of xtra STR'),
            Item(AbilitySetter(resource=ABILITY.STR, score=23), name='Giants belt'),
            Item(AbilityMaxSetter(ability=ABILITY.STR, score=24), name='Gauntlets of extra max STR')
        ]
    )

    ab_overseer = AbilityOverseer(ch)
    ab_overseer.calculate_ability_scores()
    assert ch.abilities[ABILITY.STR].score == 23
