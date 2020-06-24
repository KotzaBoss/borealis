from __future__ import annotations

from components import Component


class Stealth(Component):
    def __init__(self, stealth=False):
        self._stealth: bool = stealth

    @property
    def stealth(self):
        return self._stealth

    @stealth.setter
    def stealth(self, value: bool):
        self._stealth = value

    def update(self, char: Character):
        pass
