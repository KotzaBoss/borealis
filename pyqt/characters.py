"""
This module will contains the character class and functions associated with:

Creating, saving, deleting, characters.
"""
import json
import os
from typing import Optional

from PyQt5 import QtWidgets as widg

# from . import TOP_DIR
from .classes import CLASSES
from .common import Win
from .races import RACES
from .utils import init_stat_roll


class IncompatibleVersion(Exception):
    pass


class DeathSaves(dict):
    """ `dict` subclass to overload `+` operator"""

    def __add__(self, other):
        """ Add common key values of `other` to `self` """
        if other:
            for key in self.keys():
                self[key] += other[key]


CHARACTERS = {}

SKILLS = {'acrobatics': {'stat': 'dex'},
          'animal handling': {'stat': 'wis'},
          'arcana': {'stat': 'int'},
          'athletics': {'stat': 'str'},
          'deception': {'stat': 'cha'},
          'history': {'stat': 'int'},
          'insight': {'stat': 'wis'},
          'intimidation': {'stat': 'cha'},
          'investigation': {'stat': 'int'},
          'medicine': {'stat': 'wis'},
          'nature': {'stat': 'int'},
          'perception': {'stat': 'wis'},
          'performance': {'stat': 'cha'},
          'persuasion': {'stat': 'cha'},
          'religion': {'stat': 'int'},
          'sleight of hand': {'stat': 'dex'},
          'stealth': {'stat': 'dex'},
          'survival': {'stat': 'wis'},
          }

def set_skills(stats, class_):
    try:
        char_skill_score_stat = {skill: {'score': stats[skill_score_stat['stat']]['mod'],
                                         'stat': skill_score_stat['stat'],
                                         'prof': False}
                                 for skill, skill_score_stat in SKILLS.items()}
        Win.memwin.insertPlainText(f"choose {CLASSES[class_]['skill_prof']['num']} from\n"
                                   f"{CLASSES[class_]['skill_prof']['skills']} with <enter>", prompt=False)
        for _ in range(CLASSES[class_]['skill_prof']['num']):
            skill = cmdline_input(prompt=False).strip()
            while True:
                if skill in CLASSES[class_]['skill_prof']['skills']:
                    mem_output(f"{skill}", prompt=False)
                    char_skill_score_stat[skill]['score'] += 2
                    char_skill_score_stat[skill]['prof'] = True
                    break
                else:
                    skill = cmdline_input(f"Skill not found try again").strip()
        else:
            return char_skill_score_stat
    except Exception as e:
        err_output(f"{e.__traceback__.tb_lineno} {e}")


def init_hp(stats, class_):
    return {'max': CLASSES[class_]['init_hp'] + stats[CLASSES[class_]['lvlup_mod']]['mod'],
            'curr': CLASSES[class_]['init_hp'] + stats[CLASSES[class_]['lvlup_mod']]['mod'],
            'hit_dice': CLASSES[class_]['hit_dice'],
            'lvlup_mod': CLASSES[class_]['lvlup_mod']}


def show_character(name: Optional[str] = None, attr: Optional[str] = None):
    """ Show all or one of the available characters """
    if CHARACTERS:
        if not name:
            mem_output()
            for name in CHARACTERS:
                mem_output(f"{CHARACTERS[name]}", prompt=False)
        elif name in CHARACTERS:
            if not attr:
                mem_output(f"{CHARACTERS[name]}", prompt=True)
            elif attr in dir(CHARACTERS[name]):
                mem_output(f"Name: {CHARACTERS[name].name}\n"
                           f"{attr}: {getattr(CHARACTERS[name], attr)}",
                           prompt=True)
            else:
                err_output(f"Character's {name} attribute not found")
    else:
        mem_output(f"No characters available", prompt=False)


def create_character():
    """ Read name race class of character and throw initial rolls and skills and save character file """

    name = choose_name()
    race = choose_race(name)
    class_ = choose_class(name)
    init_stats = init_stat_roll(race, class_)
    init_skills = set_skills(init_stats, class_)
    CHARACTERS[name] = Character(init=True, name=name, race=race, class_=class_, init_stats=init_stats,
                                 init_skills=init_skills)
    save_character(CHARACTERS[name])


def read_character():
    """ Read json file from `ExperimentDirectory/char_storage` folder"""
    files = os.listdir(os.path.join(TOP_DIR, 'char_storage'))
    try:
        for file in files:
            with open(os.path.join(TOP_DIR, f"char_storage/{file}"), 'r') as f:
                json_ = json.load(f)
                if json_['version'] != Character._version:
                    raise IncompatibleVersion('Incompatible JSON file')
                CHARACTERS[json_['name']] = Character.from_json(json_=json_)

    except FileNotFoundError:
        err_output(f"Error reading files")

    except IncompatibleVersion as IV:
        err_output(f"{IV}")


def delete_character(name: str):
    """ Pop character fro `CHARACTERS` and delete character file """
    if name in CHARACTERS:
        CHARACTERS.pop(name)
        os.remove(os.path.join(TOP_DIR, f"char_storage/{name}.json"))
    else:
        err_output(f"{name} not found")


def save_character(character):
    """ Save character in json file """
    with open(os.path.join(TOP_DIR, f"char_storage/{character.name}.json"), 'w') as outfile:
        json.dump(character.__dict__,
                  outfile,
                  indent=10,
                  ensure_ascii=False
                  )


class Character(object):
    """ TODO:

        - [ ] Implement inventory
        - [~] Implement weapons

          Should weapons, armor, inv be separate? (i guess so)

        - [ ] Make cross-character dynamic changes.
          i.e. if player gets smth that changes stats then
          immediate changes to all mods and skill must happen automatically (how?)

        - Understand the connections between stats-skills-armor...
    """

    _version = '0.5.4ds'

    def __init__(self, json_=None, **kargs):
        if json_:
            self.json_character(json_)
        else:
            self.new_character(**kargs)

        # only to print attributes in custom order
        self.__dict__ = {'version': self.version,
                         'name': self.name,
                         'status': self.status,
                         'cond': self.cond,
                         'lvl': self.lvl,
                         'ac': self.ac,
                         'race': self.race,
                         'class_': self.class_,
                         'prof': self.prof,
                         'damage': self.damage,
                         'speed': self.speed,
                         'hp': self.hp,
                         'stats': self.stats,
                         'skills': self.skills,
                         'features': self.features,
                         'armor': self.armor,
                         'weapons': self.weapons,
                         'saves': self.saves
                         }

    @classmethod
    def from_json(cls, json_):  # Constructor from json
        return cls(json_=json_)

    def json_character(self, json_):
        self.name = json_['name']
        self.status = json_['status']
        self.cond = json_['cond']
        self.lvl = json_['lvl']
        self.ac = json_['ac']
        self.race = json_['race']
        self.class_ = json_['class_']
        self.prof = json_['prof']
        self.damage = json_['damage']
        self.speed = json_['speed']
        self.hp = json_['hp']
        self.stats = json_['stats']
        self.skills = json_['skills']
        self.features = json_['features']
        self.armor = json_['armor']
        self.weapons = json_['weapons']
        self.saves = DeathSaves(json_['saves'])
        self.version = json_['version']

    def new_character(self, **kargs):
        self.lvl = 1
        self.name = kargs['name']
        self.status = 'alive'
        self.cond = None
        self.race = kargs['race']
        self.class_ = kargs['class_']
        self.stats = kargs['init_stats']
        self.skills = kargs['init_skills']
        self.prof = {'score': CLASSES[self.class_]['lvls'][1]['prof'],
                     'armors': CLASSES[self.class_]['skill_prof']['armor'],
                     'weapons': CLASSES[self.class_]['skill_prof']['weapons']}
        self.hp = init_hp(self.stats, self.class_)
        self.armor = CLASSES[self.class_]['armor']
        num, stat = CLASSES[self.class_]['armor']['ac'].split('+')
        self.ac = int(num) + self.stats[stat]['mod']
        self.weapons = {weapon['name']: weapon for weapon in CLASSES[self.class_]['weapons']}
        self.features = CLASSES[self.class_]['lvls'][1]['features']
        self.damage = RACES[kargs['race']]['damage']
        self.speed = RACES[kargs['race']]['speed']
        self.saves = DeathSaves({'success': 0,
                                 'failures': 0})
        self.version = Character._version

    #
    # def receive(self, att, dmg, dmg_type, dist):
    #     """ DM says enemy attack roll and dmg roll and type"""
    #     assert re.search(r"\d+", att), 'Expected att as integer'
    #     assert re.search(r"\d+", dmg), 'Expected dmg as integer'
    #     assert dmg_type in DMG_TYPES, 'Unavailable damage type'
    #
    #     att = int(att)
    #     dmg = int(dmg)
    #
    #     # CHECK STATUS
    #     if self.status == 'unconscious':
    #         self.saves + death_save_roll(dist=dist)  # <-- op overload in DeathSaves(dict) class in characters.py
    #         if self.saves['success'] == 3:
    #             mem_output(f"STABLE")
    #             self.status = 'stable'
    #             self.hp['curr'] = 0
    #             return
    #         elif self.saves['failures'] == 3:
    #             mem_output(f"DEAD")
    #             self.status = 'dead'
    #             self.hp['curr'] = 0
    #             return
    #     elif self.status == 'dead':
    #         mem_output(f"I guess someone is beating a dead horse.")
    #         return
    #
    #     # AC COMPARE
    #     if att < self.ac:
    #         mem_output(f"Miss")
    #         return
    #
    #     else:
    #         # DMG TYPE
    #         const = 1
    #         if self.damage['resist']:
    #             if dmg_type in self.damage['resist']:
    #                 const = 0.5
    #         elif self.damage['vulnerable']:
    #             if dmg_type in self.damage['vulnerable']:
    #                 const = 2
    #         elif self.damage['immune']:
    #             if dmg_type in self.damage['immune']:
    #                 const = 0
    #         dmg *= const
    #         dmg = int(dmg)  # cut float part since dnd rounds down no matter the digit:
    #         #                                           1.1 -> 1
    #         #                                           1.5 -> 1
    #         #                                           1.8 -> 1
    #     self.hp['curr'] -= dmg
    #
    #     if self.hp['curr'] <= (-self.hp['max']):
    #         mem_output(f"DEAD")
    #         self.status = 'dead'
    #     elif self.hp['curr'] <= 0:
    #         mem_output(f"UNCONSCIOUS")
    #         self.status = 'unconscious'
    #     else:
    #         mem_output(health_bar(self.hp['curr'], self.hp['max']))
    #
    # def combat(self):
    #     """ Read json file and perfrom attack and damage rolls """
    #     str_ = ''
    #     for weapon in self.weapons:
    #         str_ += f"{weapon}:\n"
    #         for attr_name, attr_value in self.weapons[weapon].items():
    #             if attr_name == 'name':
    #                 continue
    #             str_ += f"\t{attr_name}: {attr_value}\n"
    #     else:
    #         str_ += f"{50 * '-'}"
    #
    #     mem_output(f"{str_}", prompt=False)
    #     while True:
    #         output = CombatOutput()
    #         output.char = CHARACTERS[self.name]
    #         try:
    #             output.weapon = cmdline_input(f"weapon choice")
    #
    #         except KeyError as KE:
    #             err_output(f"{KE}")
    #         else:
    #             while True:
    #                 try:
    #                     if 'finesse' in self.weapons[output.weapon]['properties']:
    #                         mem_output(
    #                             f"Choose AM. str: {self.stats['str']['mod']}, dex: {self.stats['dex']['mod']}")
    #                         output.stat = cmdline_input()
    #                     else:
    #                         output.stat = 'str'
    #                 except KeyError as KE:
    #                     err_output(f"{KE}")
    #                 else:
    #                     if output.attack_roll():
    #                         output.damage_roll()
    #                     del output
    #                     return

    def __repr__(self):
        return f"version: {self.version}\n" \
               f"name: {self.name}\n" \
               f"hp: {self.hp}\n" \
               f"status: {self.status}\n" \
               f"class: {self.class_}\n" \
               f"saves: {self.saves}"


def health_bar(curr, max_):
    bar_len = 30
    percent = int((bar_len * curr) / max_)
    return f"{curr}/{max_}\n" \
           f"[{percent * '-'}{(bar_len - percent) * 'x'}]"


def choose_name():
    name = widg.QInputDialog.getText(Win.cmdline, "Name", "What is your name?")
    print(name)
    return name[0]


def choose_race(name):
    race = \
        widg.QInputDialog.getText(Win.cmdline, 'Race',
                                  f"What is {name}'{'' if name[-1] in ('s', 'S') else 's'} race: ")[0]
    while True:
        if race not in RACES:
            race = widg.QInputDialog.getText(Win.cmdline, 'Race', 'Unavailable race try again')[0]
        else:
            return race


def choose_class(name):
    class_ = \
        widg.QInputDialog.getText(Win.cmdline, 'Race',
                                  f"What is {name}'{'' if name[-1] in ('s', 'S') else 's'} class: ")[0]
    while True:
        if class_ not in CLASSES.keys():
            # class_ = cmdline_input(f"Unavailable class try again: ", prompt=False)
            class_ = widg.QInputDialog.getText(Win.cmdline, 'Race', 'Unavailable class')[0]
        else:
            return class_
