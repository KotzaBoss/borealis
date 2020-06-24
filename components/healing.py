from __future__ import annotations

from components import Component


class Healing(Component):
    def __init__(self, heal_points: int = 0):
        if type(heal_points) != int:
            raise TypeError("Heal points must be int.")
        self._heal_points = heal_points

    @property
    def heal_points(self):
        return self._heal_points

    @heal_points.setter
    def heal_points(self, heal_points):
        self._heal_points = heal_points

    def update(self, char: Character):
        pass
