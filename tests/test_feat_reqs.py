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
    f = Feat(*requirement)
    c = Character(feats=[f], proficiencies=[Proficiency(ARMORTYPE.HEAVY),
                                            Proficiency(ARMORTYPE.LIGHT)])  # TODO: make proficiency get multiple profs?
    for comp in f.components:
        if isinstance(comp, AbilityRequirement):
            for ability in comp.requirement:
                if c.abilities[ability.name] >= ability.score:
                    assert passed is True
                    print(
                        f"\nfrom components {f.components} ~ abilities {[f'{abil[0]}-{abil[1].score}' for abil in c.abilities.items()]}\n"
                        f"{c.abilities[ability.name]} is >= {ability.score}")
                    return
            else:
                print(
                    f"\nfrom components {f.components} ~ abilities {[f'{abil[0]}-{abil[1].score}' for abil in c.abilities.items()]}\n"
                    f"no ability is >= {ability.score}")
                assert passed is False
                return
        else:
            for prof in comp.requirement:
                if prof in c.proficiencies:
                    print(f"\n{prof} in {c.proficiencies}")
                    assert passed is True
                    return
            else:
                print(f"\n{prof} not in {c.proficiencies}")
                assert passed is False
                return

    assert False, "Doubt it should reach this line"
