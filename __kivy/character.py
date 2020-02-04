import json

import requests
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

from .common import DeathSaves, IncompatibleVersion
from .common.skills import SKILLS
from .common.utils import STATS, init_stat_roll, finalise_init

CHARACTERS = {}

class Character(object):
    """ TODO:

        - [ ] Implement inventory
        - [ ] Implement weapons

          Should weapons, armor, inv be separate? (i guess so)

        - [ ] Make cross-character dynamic changes.
          i.e. if player gets smth that changes stats then
          immediate changes to all mods and skill must happen automatically (how?)

        - Understand the connections between stats-skills-armor...
    """

    _version = '0.5.5req'

    def __init__(self, json_=None, **kargs):
        if json_:
            self.json_character(json_)
        else:
            self.new_character(**kargs)

    @classmethod
    def from_json(cls, json_):  # Constructor from json
        return cls(json_=json_)

    def json_character(self, json_):
        for key in json_:
            setattr(self, str(key), json_[key])
        self.saves = DeathSaves(self.saves)

    def new_character(self, **kwargs):
        class_init = json.loads(requests.get(f"https://www.dnd5eapi.co/api/classes/{kwargs['class_']}").text)
        race_init = json.loads(requests.get(f"https://www.dnd5eapi.co/api/races/{kwargs['race']}").text)
        class_lvl_init = json.loads(
            requests.get(f"https://www.dnd5eapi.co/api/classes/{kwargs['class_']}/levels/1").text)

        self.lvl = 1
        self.name = kwargs['name']
        self.status = 'alive'
        self.cond = None
        self.race = kwargs['race']
        self.class_ = kwargs['class_']
        self.stats = kwargs['init_stats']
        self.skills = kwargs['init_skills']
        self.prof = {'score': class_lvl_init['prof_bonus'],
                     'class_profs': class_init['proficiencies'],
                     'race_profs': race_init['starting_proficiencies']}
        self.hp = init_hp(self.stats, self.class_)
        self.armor = '<PLACEHOlDER>'
        num, stat = '10', 'con'  # placeholders
        self.ac = int(num) + self.stats[stat]['mod']
        self.weapons = {'<PLACEHONDER>': "api/startingweapons"}  # api doesnt have them
        self.features = class_lvl_init['features']
        self.class_specific = class_lvl_init['class_specific']
        self.damage = '<PLACEHOLDER>'
        self.speed = race_init['speed']
        self.size = race_init['size']
        self.languages = race_init['languages']
        self.traits = race_init['traits']
        self.saves = DeathSaves({'success': 0,
                                 'failures': 0})
        self.version = Character._version

    def __str__(self):
        return str(self.__dict__)

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


classes = json.loads(requests.get('https://www.dnd5eapi.co/api/classes').text)
for class_ in classes['results']:
    setattr(ClassChoice, f"{class_['name'].lower()}", ObjectProperty(None))
del classes


class RaceChoice(Screen):
    def btn(self, btn_text):
        CharCreate._race = btn_text.lower()


races = json.loads(requests.get('https://www.dnd5eapi.co/api/races').text)
for race in races['results']:
    setattr(RaceChoice, f"{race['name'].lower()}", ObjectProperty(None))
del races


class SkillChoice(Screen):

    def setup(self):
        class_init = json.loads(requests.get(f"https://www.dnd5eapi.co/api/classes/{CharCreate._class.lower()}").text)

        self.choices = 0
        self.max_choices = class_init['proficiency_choices'][0]['choose']
        self.char_skill_score_stat = {skill: {'score': CharCreate._init_stats[skill_score_stat['stat']]['mod'],
                                              'stat': skill_score_stat['stat'],
                                              'prof': False}
                                      for skill, skill_score_stat in SKILLS.items()}

        self.mega_layout.add_widget(Label(text=f"Choose {self.max_choices}",
                                          size_hint_y=None,
                                          height=100))

        # self.mega_layout.add_widget(Label(text=f"Choose {CLASSES[CharCreate._class]['skill_prof']['num']}",
        #                                   size_hint_y=None,
        #                                   height=100))
        # for skill in CLASSES[CharCreate._class]['skill_prof']['skills']:
        for skill in class_init['proficiency_choices'][0]['from']:
            skillbtn = Button(text=f"{skill['name'].split(' ', maxsplit=1)[1].lower()}")
            skillbtn.bind(on_press=self.set_skills)
            self.prime_layout.add_widget(skillbtn)

    def set_skills(self, btn):
        self.choices += 1
        btn.disabled = True
        self.char_skill_score_stat[btn.text]['score'] += 2
        self.char_skill_score_stat[btn.text]['prof'] = True
        if self.choices == self.max_choices:
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
    class_init = json.loads(requests.get(f'https://www.dnd5eapi.co/api/classes/{class_}').text)
    return {'max': class_init['hit_die'] + stats['con']['mod'],
            'curr': class_init['hit_die'] + stats['con']['mod'],
            'hit_dice': f"1d{class_init['hit_die']}",
            'lvlup_mod': 'con'}  # <-- couldnt find in api


def save_character(character):
    """ Save character in json file """
    with open(f"char_storage/{character.name}.json", 'w') as outfile:
        json.dump(character.__dict__,
                  outfile,
                  indent=10,
                  ensure_ascii=False
                  )
