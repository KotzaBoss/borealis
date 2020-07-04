from __future__ import annotations

from components import Component


class ScoreManipulator(Component):
    """ Base class for any object that changes a resource.
    `resource` may be an ability, that should be manipulated by the `score`

    Who should provide the logic behind the manipulation? The overseer?

    The resource could be just a class type allowing checks to be with the is operator
    for better readability and less memory use since we wont be instantiating anything as a resource

    Check tests for use.
    """

    def __init__(self, score: int = 0, resource=None):
        self._score = score
        self._resource = resource

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score: int):
        self._score = score

    @property
    def resource(self):
        return self._resource

    @resource.setter
    def resource(self, resource):
        self._resource = resource

    def update(self, char: Character):
        pass


class Setter(ScoreManipulator):
    pass


class Changer(ScoreManipulator):
    pass


class MaxSetter(ScoreManipulator):
    pass
