"""
Due to circular dependency between Character, Components, ComponentCollections type hinting,
Most files have

`from __future__ import annotations`

at the top to postpone evaluation of type hints.

If you want your IDE to stop complaining about type hints not being imported,
add the following after the `__future__` import

>>> from typing import TYPE_CHECKING
>>> if TYPE_CHECKING:
>>>     from module import Type
>>> # rest of code

"""

DEBUG = True
