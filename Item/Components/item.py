class Item(object):
    """ Used for any item (weapon, armor, ring, ...) acquired by the player. """

    def __init__(self, components: dict = None):
        if not components:
            components = {}
        self._components = components

    def insert_component(self, *component):
        for comp in component:
            self.components[comp.__class__.__name__] = comp

    @property
    def components(self):
        return self._components

    @components.setter
    def components(self, components):
        self._components = components

    def __repr__(self):
        ret = ''
        for _comp, val in self.components.items():
            ret += f"{_comp}:\n{val}\n"
        return ret
