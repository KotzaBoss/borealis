from enums import ABILITY
from item.components import Component, Bollean


class Requirement(Component):
    def __init__(self, requirement, **kwargs):
        super().__init__(**kwargs)  # forward keyword arguments (used by Bollean class)
        self._requirement = requirement

    @property
    def requirement(self):
        return self._requirement

    @requirement.setter
    def requirement(self, requirement):
        self._requirement = requirement

    def update(self, char_sheet: dict):
        pass


class AbilityRequirement(Requirement):
    def __init__(self, value=-666, ability: ABILITY = ABILITY.NONE):
        super().__init__({'value': value, 'ability': ability})

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return f"{self._requirement['ability'].name} > {self._requirement['value']}"


class Attunement(Requirement, Bollean):
    def __init__(self, attunement: bool = False):
        super().__init__(attunement, bvalue=attunement)

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return str(self._requirement)
