from character import Character, AbilityOverseer
from item import Item
from item.components.score_manipulator import ScoreSetter, ScoreChanger, ScoreMaxSetter
from utils.enums import ABILITY


def test_foo():
    ch = Character(  # for init_items=None stats have std roll
        items=[
            Item(ScoreChanger(ability=ABILITY.STR, score=3), name='Ring of xtra STR'),
            Item(ScoreSetter(ability=ABILITY.STR, score=23), name='Giants belt'),
            Item(ScoreMaxSetter(ability=ABILITY.STR, score=24), name='Gauntlets of extra max STR')
        ]
    )

    ab_overseer = AbilityOverseer(ch)
    ab_overseer.calculate_ability_scores()
    assert ch.abilities[ABILITY.STR].score == 23
