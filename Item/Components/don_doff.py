from duration import Duration
from .component import Component


class Don(Component, Duration):
    def __init__(self, duration=-1):
        super().__init__(duration)


class Doff(Component, Duration):
    def __init__(self, duration=-1):
        super().__init__(duration)
