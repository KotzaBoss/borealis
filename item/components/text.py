from . import Component


class Text(Component):
    def __init__(self, txt=''):
        self._text: str = txt

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, string: str):
        self._text = string

    def update(self, char_sheet: dict):
        pass

    def __repr__(self):
        return self.text