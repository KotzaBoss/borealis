import json

from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

from .common import DeathSaves, IncompatibleVersion
from .common.classes import CLASSES
from .common.races import RACES
from .common.skills import SKILLS
from .common.utils import STATS, init_stat_roll, finalise_init

CHARACTERS = {}


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

    _version = '0.5.4kv'

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


class CharCreate(Screen):
    load_failure_state = BooleanProperty(False)
    load_failure_msg = StringProperty('')

    name_input = ObjectProperty(None)
    name_pop = ObjectProperty(None)

    _name = ''
    _race = ''
    _class = ''
    _init_stats = None
    _init_skills = SKILLS

    def get_name(self, input_name):
        CharCreate._name = input_name
        self.name_pop.dismiss()

    def read_character(self):
        """ Read json file from `ExperimentDirectory/char_storage` folder"""
        import os
        files = os.listdir('char_storage')
        try:
            for file in files:
                with open(f"char_storage/{file}", 'r') as f:
                    json_ = json.load(f)
                    if json_['version'] != Character._version:
                        raise IncompatibleVersion('Incompatible JSON file')
                    CHARACTERS[json_['name']] = Character.from_json(json_=json_)

        except FileNotFoundError:
            self.load_failure_state = True
            self.load_failure_msg = f"Error reading files"
            print(f"Error reading files")

        except IncompatibleVersion as IV:
            self.load_failure_state = True
            self.load_failure_msg = f"Incompatible character version"
            print(self.load_failure_msg)


class ClassChoice(Screen):
    def btn(self, btn_text):
        CharCreate._class = btn_text.lower()


for i in {'Barbarian', 'Monk', 'Rogue', 'Ranger', 'Wizard', 'Sorcerer', 'Cleric', 'Paladin'}:
    setattr(ClassChoice, f"{i}", ObjectProperty(None))


class RaceChoice(Screen):
    def btn(self, btn_text):
        CharCreate._race = btn_text.lower()


for i in {'Elf', 'Human', 'Gnome', 'Dwarf', 'Dragonborn', 'Half_orc', 'Tiefling', 'Aaracokra'}:
    setattr(RaceChoice, f"{i}", ObjectProperty(None))


class SkillChoice(Screen):

    def setup(self):
        self.choices = 0
        self.char_skill_score_stat = {skill: {'score': CharCreate._init_stats[skill_score_stat['stat']]['mod'],
                                              'stat': skill_score_stat['stat'],
                                              'prof': False}
                                      for skill, skill_score_stat in SKILLS.items()}

        self.mega_layout.add_widget(Label(text=f"Choose {CLASSES[CharCreate._class]['skill_prof']['num']}",
                                          size_hint_y=None,
                                          height=100))

        for skill in CLASSES[CharCreate._class]['skill_prof']['skills']:
            skillbtn = Button(text=f"{skill}")
            skillbtn.bind(on_press=self.set_skills)
            self.prime_layout.add_widget(skillbtn)

    def set_skills(self, btn):
        self.choices += 1
        btn.disabled = True
        self.char_skill_score_stat[btn.text]['score'] += 2
        self.char_skill_score_stat[btn.text]['prof'] = True
        if self.choices == 2:
            CharCreate._init_skills = self.char_skill_score_stat
            self.manager.current = 'main'
            CHARACTERS[CharCreate._name] = Character(init=True,
                                                     name=CharCreate._name,
                                                     race=CharCreate._race,
                                                     class_=CharCreate._class,
                                                     init_stats=CharCreate._init_stats,
                                                     init_skills=CharCreate._init_skills)
            save_character(CHARACTERS[CharCreate._name])


class InitRoll(Screen):

    def getcolumns(self):
        self.c1, self.c2 = init_stat_roll()
        self.prefinal_stats = STATS

        self.alloc.bind(on_press=self.finalise)
        self.alloc.disabled = True

        for i, (stat, n1, n2) in enumerate(zip(STATS, self.c1, self.c2)):
            self.stat_col.add_widget(Label(id=f"{stat}",
                                           text=f"{stat}",
                                           color=(0, 1, 1, 1))
                                     )

            txtinput = TextInput(id=f"inp{stat}", multiline=False)
            txtinput.bind(on_text_validate=self.getname)
            self.input_col.add_widget(txtinput)

            check = CheckBox(id=f"check{stat}")
            self.checkbox.add_widget(check)
            self.col1.add_widget(Button(id=f"r{stat}c3",
                                        text=f"{n1}"))

            self.col2.add_widget(Button(id=f"r{stat}c4",
                                        text=f"{n2}"))

    def getname(self, txtinput):
        try:
            index = None
            for i, check in enumerate(self.checkbox.children):
                if check.id == f"check{txtinput.id[-3:]}":
                    index = i

            if int(txtinput.text) in self.c1 + self.c2:
                self.checkbox.children[index].active = True
                self.prefinal_stats[txtinput.id[-3:]]['score'] = int(txtinput.text)
            else:
                self.checkbox.children[index].active = False
                self.prefinal_stats[txtinput.id[-3:]]['score'] = 0

        except ValueError as v:
            print(v)

        else:
            self.validate()

    def validate(self):
        if all([child.active for child in self.checkbox.children]):
            self.alloc.disabled = False
        else:
            self.alloc.disabled = True

    def finalise(self, btn):
        CharCreate._init_stats = finalise_init(CharCreate._race, CharCreate._class, self.prefinal_stats)
        CHARACTERS[CharCreate._name] = Character(init=True,
                                                 name=CharCreate._name,
                                                 race=CharCreate._race,
                                                 class_=CharCreate._class,
                                                 init_stats=CharCreate._init_stats,
                                                 init_skills=CharCreate._init_skills)


def init_hp(stats, class_):
    return {'max': CLASSES[class_]['init_hp'] + stats[CLASSES[class_]['lvlup_mod']]['mod'],
            'curr': CLASSES[class_]['init_hp'] + stats[CLASSES[class_]['lvlup_mod']]['mod'],
            'hit_dice': CLASSES[class_]['hit_dice'],
            'lvlup_mod': CLASSES[class_]['lvlup_mod']}


def save_character(character):
    """ Save character in json file """
    with open(f"char_storage/{character.name}.json", 'w') as outfile:
        json.dump(character.__dict__,
                  outfile,
                  indent=10,
                  ensure_ascii=False
                  )
