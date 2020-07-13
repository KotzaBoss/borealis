class Score(list):
    """ Class to be used for most numbers.
        A Score is a list of objects that contribute to a final number
        Each object should supply their arithmetic magic methods.
        >>> from ability import Ability
        >>> s1 = Score(Ability(base=15))
        >>> s2 = Score(Ability(base=5))
        >>> s1 + s2
        20

        Raises
        ------
        AttributeError
            When list elements do not support arithmetic operations
    """

    def __init__(self, *args):
        """
            Parameters
            ----------
            args
                Initial objects that implement arithmetic operators
        """
        if args:
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
        return f"Score({super().__repr__()}={sum(self)})"
