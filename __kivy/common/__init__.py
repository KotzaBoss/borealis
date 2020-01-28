class DeathSaves(dict):
    """ `dict` subclass to overload `+` operator"""

    def __add__(self, other):
        """ Add common key values of `other` to `self` """
        if other:
            for key in self.keys():
                self[key] += other[key]


class IncompatibleVersion(Exception):
    pass
