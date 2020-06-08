from item.components import Component
from utils.enums import ABILITY


class ScoreManipulator(Component):
    def __init__(self, score: int = 0, ability: ABILITY = None):
        self._score = score
        self._ability = ability

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score: int):
        self._score = score

    @property
    def ability(self):
        return self._ability

    @ability.setter
    def ability(self, ability: ABILITY):
        self._ability = ability

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return f"{self._score} {self._ability.name}"


class ScoreSetter(ScoreManipulator):
    def __init__(self, score: int = 0, ability=None):
        super().__init__(score=score, ability=ability)


class ScoreChanger(ScoreManipulator):
    def __init__(self, score: int = 0, ability=None):
        super().__init__(score=score, ability=ability)


class ScoreMaxSetter(ScoreManipulator):
    def __init__(self, score: int = 0, ability=None):
        super().__init__(score=score, ability=ability)
