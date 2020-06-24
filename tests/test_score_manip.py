import pytest

from character import Character, Ability, ABILITY
from components.score_manipulator import Setter, MaxSetter, Changer
from item import Item
from overseer import AbilityOverseer


@pytest.mark.parametrize(
    'manipulator, score', [
        (Changer(score=10, resource=Ability(name=ABILITY.STR)), 25),
        (Setter(score=10, resource=Ability(name=ABILITY.STR)), 10),
        (MaxSetter(score=10, resource=Ability(name=ABILITY.STR)), 10)
    ]
)
def test_score_manip(manipulator, score):
    ch = Character(
        items=[Item(manipulator)]
    )
    AbilityOverseer.calculate_ability_scores(ch)
    if isinstance(manipulator, MaxSetter):
        num = ch.abilities[ABILITY.STR].max
    else:
        num = ch.abilities[ABILITY.STR].score
    assert num == score
