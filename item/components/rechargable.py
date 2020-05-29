from item.components import Component, Bollean


class Rechargeable(Component, Bollean):
    def __init__(self, bvalue: bool = False):
        super().__init__(bvalue)

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return str(self._bvalue)
