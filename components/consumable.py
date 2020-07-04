from __future__ import annotations

from components import Component, Boolean


class Consumable(Component, Boolean):
    def __init__(self):
        super().__init__()

    def update(self, char: Character):
        pass

    def __bool__(self):
        return True
