""" Module containing all item components providing Duration

Taking note from the python.collections all durations are defined in the __init__.py module
simplifying the import command

from:
    from item.components.durations.g.specific_duration_module import SpecificDuration
to:
    from item.components.durations.g import SpecificDuration
"""

from item.components import Component


class Duration(Component):
    """ Time Duration class. Can be used for any time durations needs. """

    def __init__(self, duration: int = -1):
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return str(self._duration)


class Don(Duration):
    def __init__(self, duration=-1):
        super().__init__(duration)


class Doff(Duration):
    def __init__(self, duration=-1):
        super().__init__(duration)


class EffectDuration(Duration):
    def __init__(self, duration=-1):
        super().__init__(duration)
