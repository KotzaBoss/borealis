from pprint import pformat


class Score(list):
    """ Class to be used for most numbers.
        A Score is a list of objects that contribute to a final number
        Each object should supply their arithmetic magic methods.

        Raises
        ------
        AttributeError
            When list elements do not support arithmetic operations
    """

    def __init__(self, *args):
        for obj in args:
            if not all(method in dir(obj) for method in ['__add__', '__radd__']):  # Ensure arithmetic ops are implemented
                raise AttributeError
        super().__init__(args)

    def __add__(self, other):
        return sum(self) + other

    def __radd__(self, other):
        return sum(self) + other

    def calc(self):
        return sum(self)

    def __repr__(self):
        return "Score(" + pformat(super().__repr__()).strip('()').replace("'", '') + f"={sum(self)})"
