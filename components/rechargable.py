from __future__ import annotations

from components import Component, Boolean


class Rechargeable(Component, Boolean):
    def __init__(self):
        super().__init__()

    def __bool__(self):
        return True

    def update(self, char: Character):
        pass
