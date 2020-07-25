from __future__ import annotations

import sys
from abc import ABC, abstractmethod
from typing import Dict, List, Type, Callable, Set

from character import Character
from overseer import AbilityOverseer
from overseer import Overseer
from utils.resources import ABILITY
from utils.resources import Resource
from utils.resources import isresource
from utils.roll import roll


def get_overseer_class(resource):
    if isresource(resource, ABILITY):
        return AbilityOverseer
    else:
        pass  # TODO: rest of resources


class Overlord(ABC):
    """ Overloard Abstract Base Class """

    @classmethod
    @abstractmethod
    def awaken(cls, *args, **kwargs):
        pass


class Amun(Overlord):
    """ He the one who creates. """

    @classmethod
    def awaken(cls, *args, **kwargs):
        """ Create new character.
            TODO: Nail down logic for character creation
        """
        ch = Character(*args, **kwargs)
        over = AbilityOverseer(ch)
        if items := kwargs.get('items', None):
            over.add_dep(*items)
        StorageGod.add_char(ch)
        StorageGod.add_overseer(ch, over)
        return ch


class Horus(Overlord):
    """ He sees all. """

    @classmethod
    def awaken(cls, char: Character, resource: Type[Resource]):
        """ Generate final score/frame of resource requested. """
        if isresource(resource, ABILITY):
            over = StorageGod.get_overseer(char, get_overseer_class(resource))
            if isinstance(resource, type):
                return {ability: (over.calc(ability), over.deps[ability]) for ability in ABILITY}
            else:
                return {resource: over.calc(resource)}, over.deps[resource]
        else:
            return char[resource]


class StorageGod(Overlord):
    """ He who keeps stuff.

        For every character a set of Overseer. Set because it doesnt make sense to have
        multiple Overseers of the same type.
    """
    characters: Dict[Character, Set[Overseer]] = {}

    @classmethod
    def awaken(cls, *args, **kwargs):
        pass

    @classmethod
    def add_char(cls, char):
        cls.characters[char] = set()

    @classmethod
    def add_overseer(cls, char, overseer):
        cls.characters[char].add(overseer)

    @classmethod
    def delete_char(cls, char):
        cls.characters.pop(char)

    @classmethod
    def delete_overseer(cls, char, overseer):
        cls.characters[char].remove(overseer)

    @classmethod
    def get_overseer(cls, char, overseer: Type[Overseer]):
        for over in cls.characters[char]:
            if isinstance(over, overseer):
                return over
        else:
            return None


class Ares(Overlord):
    """ Man-o-war. """

    @classmethod
    def awaken(cls, *args, **kwargs):
        """ Gather troops and perform combat/action? """


class Mnemosyne(Overlord):
    """ She always remembers. """

    @classmethod
    def awaken(cls, *args, **kwargs):
        """ Read previous character and import it"""


class Daloth(Overlord):
    """ Causes insanity at the sight of his output. """

    @classmethod
    def awaken(cls, *args, **kwargs):
        """ Push output from overlords to UI. """


class Hypnos(Overlord):
    """ All fall asleep when he exits. """

    @classmethod
    def awaken(cls, *args, **kwargs):
        """ Save and exit the program. """
        sys.exit()


class Fortuna(Overlord):
    """ Hopefully she favors your rolls. """

    @classmethod
    def awaken(cls, expr, *args, **kwargs):
        """ Roll die from expr. """
        return roll(expr)


class Cthulhu(Overlord):
    """ He controls his overseers with his tentacles. """
    _overseers: List[Overseer] = [AbilityOverseer, ...]

    @classmethod
    def awaken(cls, *args, **kwargs):
        """ Whip his minions and do what needs be done."""
        pass

    @classmethod
    def loop(cls, char: Character):
        for overseer in cls._overseers:
            overseer.awaken(char)

    @classmethod
    def overseers(cls):
        return cls._overseers


class Azathoth(Overlord):
    """ Wakes from his slumber when user inputs.
    The only one with the Character sheet availlable, which he distributes to the rest.
    """
    character_storage: List[Character] = []  # TODO: Character storage moved to separete overlord StorageGod
    CASES: Dict[str, Callable] = {
        'new': Amun.awaken,
        'roll': Fortuna.awaken,
        'view': Horus.awaken,
        'exit': Hypnos.awaken,
    }

    @classmethod
    def switch(cls, param: str) -> Callable:
        return cls.CASES.get(param)

    @classmethod
    def load_storage(cls, char):
        """ Append characters to `character_storage`. """
        cls.character_storage.append(char)

    @classmethod
    def awaken(cls, uin: str, *args, **kwargs):
        """
        Parameters
        ----------
        uin : str
            Input from user
        """
        uin = uin.split()
        if uin[1:]:
            args = uin[1:] + list(args)
        return cls.switch(uin[0])(*args, **kwargs)
        # if uin == 'new':
        #     return Amun.awaken()
        # elif uin == 'roll':
        #     return Fortuna.awaken(uin.split()[1])
        # elif uin == 'view':
        #     return Horus.awaken(*args)
        # elif uin == 'exit':
        #     return Hypnos.awaken()
