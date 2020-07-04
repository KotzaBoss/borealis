import pytest

from character import Character, Ability
from components.proficiency import Proficiency
from components.requirement import AbilityRequirement, ProficiencyRequirement
from feats import Feat
from utils.enums import ABILITY, ARMORTYPE


@pytest.mark.parametrize(
    'requirement, passed', [
        ([AbilityRequirement(Ability(base=15, name=ABILITY.STR))], True),
        ([AbilityRequirement(Ability(base=50, name=ABILITY.INT), Ability(base=0, name=ABILITY.WIS))], True),
        ([AbilityRequirement(Ability(base=50, name=ABILITY.INT), Ability(base=50, name=ABILITY.WIS))], False),
        ([ProficiencyRequirement(Proficiency(ARMORTYPE.HEAVY))], True),
        ([ProficiencyRequirement(Proficiency(ARMORTYPE.MEDIUM))], False),
    ]
)
def test_feat_reqs(requirement, passed):
    feat = Feat(*requirement)
    char = Character(feats=[feat],
                     proficiencies=[Proficiency(ARMORTYPE.HEAVY),  # Unspecified init rolls means standard table for scores
                                    Proficiency(ARMORTYPE.LIGHT)])  # TODO: make proficiency get multiple profs?
    for comp in feat.components:
        if isinstance(comp, AbilityRequirement):
            for ability in comp.requirement:
                if char.abilities[ability.name] >= ability.score:
                    print(
                        f"\nfrom components {feat.components} ~ abilities {[f'{abil[0]}-{abil[1].score}' for abil in char.abilities.items()]}\n"
                        f"{char.abilities[ability.name]} is >= {ability.score}")
                    assert passed is True
                    return
            else:
                print(
                    f"\nfrom components {feat.components} ~ abilities {[f'{abil[0]}-{abil[1].score}' for abil in char.abilities.items()]}\n"
                    f"no ability is >= {ability.score}")
                assert passed is False
                return
        else:
            for prof in comp.requirement:
                if prof in char.proficiencies:
                    print(f"\n{prof} in {char.proficiencies}")
                    assert passed is True
                    return
            else:
                print(f"\n{prof} not in {char.proficiencies}")
                assert passed is False
                return

    assert False, "Doubt it should reach this line"
