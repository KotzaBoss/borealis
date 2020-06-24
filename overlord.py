from __future__ import annotations

import sys
from abc import ABC, abstractmethod
from typing import List

from character import Character
from overseer import AbilityOverseer
from utils.roll import roll


class Overlord(ABC):
    """ Overloard Abstract Base Class """

    @classmethod
    @abstractmethod
    def awaken(cls, *args, **kwargs):
        pass


class Azathoth(Overlord):
    """ Wakes from his slumber when user inputs.
    The only one with the Character sheet availlable, which he distributes to the rest.
    """
    character_storage: List[Character] = []

    @classmethod
    def load_storage(cls, char):
        """ Append characters to `character_storage`. """
        cls.character_storage.append(char)

    @classmethod
    def awaken(cls, uin: str, key=None):
        """
        Parameters
        ----------
        uin : str
            Input from user
        key
            Unique key for active character
        """
        # if not key:
        #     return None
        if uin == 'new':
            return Amun.awaken()
        elif 'roll' in uin:
            return Fortuna.awaken(uin.split()[1])
        elif uin == 'exit':
            return Hypnos.awaken()


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
    def awaken(cls):
        """ Save and exit the program. """
        sys.exit()


class Fortuna(Overlord):
    """ Hopefully she favors your rolls. """

    @classmethod
    def awaken(cls, expr):
        """ Roll die from expr. """
        return roll(expr)


class Amun(Overlord):
    """ He the one who creates. """

    @classmethod
    def awaken(cls, *args, **kwargs):
        """ Create new character. """
        return Character()


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
