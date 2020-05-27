from .component import Component


class Requirement(Component):
    def __init__(self, requirement=-666):
        self._requirement: int = requirement

    @property
    def requirement(self):
        return self._requirement

    @requirement.setter
    def requirement(self, value):
        self._requirement = value
