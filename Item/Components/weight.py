from .component import Component


class Weight(Component):
    def __init__(self, weight=-1):
        self._weight: int = weight

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    def __repr__(self):
        return str(self._weight)
