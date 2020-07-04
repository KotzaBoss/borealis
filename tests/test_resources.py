import pytest

from character import Character
from components.score_manipulator import Changer
from components.weight import Weight
from feats import Feat
from utils.resources import Initiative, ABILITY


@pytest.mark.parametrize(
    'resource', [
        Initiative,
        ABILITY.WIS,
    ]
)
def test_resources(resource):
    ch = Character(feats=[Feat(Weight(60), Changer(score=5, resource=resource)),
                          Feat(Weight(50))
                          ])
    ch._initiative = 10
    print('\n', ch.abilities[ABILITY.WIS], ch.initiative)
    for feat in ch.feats:
        for comp in feat.components:
            if isinstance(comp, Changer) and comp.resource is resource:
                if resource is Initiative:
                    ch._initiative += comp.score
                    assert ch.initiative == 15
                    print('\ncheck initiative')
                elif resource is ABILITY.WIS:
                    ch.abilities[resource].score += comp.score
                    assert ch.abilities[resource].score == 17
                    print('\ncheck ability score')
                else:
                    assert False, 'check resource types'
    print('\n', ch.abilities[ABILITY.WIS], ch.initiative)
