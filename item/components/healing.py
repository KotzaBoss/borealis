from item.components import Component


class Healing(Component):
    def __init__(self, heal_points):
        self._heal_points = heal_points

    @property
    def heal_points(self):
        return self._heal_points

    @heal_points.setter
    def heal_points(self, heal_points):
        self._heal_points = heal_points

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return str(self._heal_points)
