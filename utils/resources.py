from abc import ABC
from typing import Type

from components.ac import AC
from components.score import Score
from utils.enums import SAVINGTHROW, ABILITY, ARMORTYPE, SKILL, WEAPONTYPE


class Resource(ABC):
    """ Abstract class for resources handled by components.

        Example from Proficiency

        >>> from components.proficiency import Proficiency
        >>> from utils.enums import ABILITY
        >>> for resource in ['STR', ABILITY.STR]:
        ...     try:
        ...         p = Proficiency(resource)
        ...     except TypeError:
        ...         print('Incorrect Arg Type')
        ...     else:
        ...         print('ok', ABILITY.STR.name)
        Incorrect Arg Type
        ok STR

        In order to declare anything as a resource you have to either subclass Resource
        or Resource.register(NewResource) as seen bellow
    """
    pass


def isresource(x, resource: Type[Resource]) -> bool:
    """ Check whether x is a valid resource. Resources are registered below. """
    iswhat = isinstance
    if isinstance(x, type):  # To ensure both Enum and Enum.foo are correctly tested
        iswhat = issubclass
    return iswhat(x, resource)


class Initiative(Score):
    def __init__(self, *init):
        super().__init__(*init)

    def __repr__(self):
        return super().__repr__().replace('Score', self.__class__.__name__)


class ProficiencyBonus(Score):
    def __init__(self, *init):
        super().__init__(*init)


class Inspiration(Score):
    def __init__(self, *init):
        super().__init__(*init)


class Speed(Score):
    def __init__(self, *init):
        super().__init__(*init)


Resource.register(Initiative)
Resource.register(ABILITY)
Resource.register(ARMORTYPE)
Resource.register(SKILL)
Resource.register(WEAPONTYPE)
Resource.register(SAVINGTHROW)
Resource.register(AC)
Resource.register(Speed)
