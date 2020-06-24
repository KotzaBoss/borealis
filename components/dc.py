from __future__ import annotations

from components import Component
from utils.enums import ABILITY


class DC(Component):
    def __init__(self, score: int = -666, ability: ABILITY = None):
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

    def update(self, char: Character):
        pass
