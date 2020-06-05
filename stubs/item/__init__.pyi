from typing import Any, List, Set, Union

from item.components import Component


class Item:
    def __init__(self, components: Union[Set[Component], List[Component], Component] = ..., name: str = ...) -> None: ...

    def insert_component(self, *component: Any) -> None: ...

    @property
    def name(self): ...

    @name.setter
    def name(self, name: Any) -> None: ...

    @property
    def components(self): ...

    @components.setter
    def components(self, components: Any) -> None: ...
