class Duration(object):
    """ Time Duration class. Can be used for any time duration needs. """

    def __init__(self, duration=-1):
        self._duration: int = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
