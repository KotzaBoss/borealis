from typing import List

from ability import Ability
from components import Component
from components import ComponentCollection
from components.advantages import Adv
from components.requirement import AbilityRequirement
from components.score_manipulator import Changer
from utils.enums import ABILITY, SKILL
from utils.resources import Initiative


class Feat(ComponentCollection):
    """ Base class for feats. """

    def __init__(self, *components, prerequisite=None, **kwargs):
        self._prerequisite = prerequisite
        super().__init__(*components, **kwargs)

    @property
    def prerequisite(self):
        return self._prerequisite

    # def __repr__(self):
    #     s = f"{self.__class__.__name__}("
    #     for k, v in self.__dict__.items():
    #         s += f"{k}={v}, "
    #     s += "\b\b)"
    #     return s


class Actor(Feat):
    def __init__(self):
        super().__init__(
            Changer(score=1, resource=ABILITY.CHA),
            Adv(resource=SKILL.DECEPTION),
            Adv(resource=SKILL.PERFORMANCE),
            name=self.__class__.__name__
        )


class Alert(Feat):
    def __init__(self):
        super().__init__(
            Changer(score=5, resource=Initiative),
            name=self.__class__.__name__
        )


class Athlete(Feat):
    def __init__(self):
        super().__init__(
            *self.custom(),
            name=self.__class__.__name__
        )

    def custom(self) -> List[Component]:
        while (uin := input('STR or DEX? ')) not in ['STR', 'DEX']:
            pass
        return [Changer(score=1, resource=ABILITY.__members__[uin])]


class DefensiveDuelist(Feat):
    def __init__(self):
        super().__init__(
            prerequisite=AbilityRequirement(Ability(name=ABILITY.DEX, base=20)),
            name=self.__class__.__name__
        )


# Experiment
# when X do Y
# when dual wielding -> ...
# when prone -> ...
# when attacking with X weapon -> ...
# ???
class State(object):
    pass


class Action(object):
    pass


class Condition(object):
    pass
