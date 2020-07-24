from abc import ABC

from components.ac import AC
from components.score import Score
from utils.enums import SAVINGTHROW, ABILITY, ARMORTYPE, SKILL, WEAPONTYPE


def isresource(x, resource):
    """ Check whether x is a valid resource. Resources are registered below. """
    if not isinstance(x, type):  # Enum.foo is not a type but it is a resource.
        return issubclass(type(x), resource)
    return issubclass(x, resource)


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


Resource.register(Initiative)
Resource.register(ABILITY)
Resource.register(ARMORTYPE)
Resource.register(SKILL)
Resource.register(WEAPONTYPE)
Resource.register(SAVINGTHROW)
Resource.register(AC)
Resource.register(Speed)
