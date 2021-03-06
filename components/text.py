from __future__ import annotations

from components import Component


class Text(Component):
    def __init__(self, txt: str = ''):
        self._text = txt

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, string: str):
        self._text = string

    def update(self, char: Character):
        pass
