from enums import ABILITY
from item.components import Component


class DC(Component):
    def __init__(self, score: int = -666, ability: ABILITY = ABILITY.NONE):
        self._score = score
        self._ability = ability

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    @property
    def ability(self):
        return self._ability

    @ability.setter
    def ability(self, ability):
        self._ability = ability

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return f"{str(self._score)} against {str(self._ability.name)}"
