from item.components import Component, Boolean


class Silvered(Component, Boolean):
    def __init__(self, bvalue: bool = False):
        super().__init__(bvalue=bvalue)

    def update(self, char_sheet: dict):
        pass
