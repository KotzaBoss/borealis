from __future__ import annotations

from components import Component


class Proficiency(Component):
    def __init__(self, resource):
        self._resource = resource

    def __eq__(self, other):
        return self._resource == other._resource

    @property
    def resource(self):
        return self._resource

    @resource.setter
    def resource(self, resource):
        self._resource = resource

    def update(self, char: Character):
        pass
