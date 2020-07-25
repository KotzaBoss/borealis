"""
Due to circular dependency between Character, Components, ComponentCollections type hinting,
Most files have

`from __future__ import annotations`

at the top to postpone evaluation of type hints.

If you want your IDE to stop complaining about type hints not being imported,
add the following after the `__future__` import

>>> import typing
>>> if typing.TYPE_CHECKING:
>>>     from X import Y  # X and Y are object names
>>> # rest of code
"""
# START: Look up feats and features and find generic similarities
# FUTURE: Exception handling
# TODO: Add feat<->meter classes
# TODO: (Use Score for values in AC Aility score etc.) Use mediator design pattern and move the logic to Overseers

DEBUG = True
