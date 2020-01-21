from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from pyqt.utils import STATS
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.checkbox import CheckBox
from pprint import pprint
from __kivy import init_roll
from pprint import pprint

from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

from __kivy import init_roll
from pyqt.utils import STATS


# class NamePopup(Popup):
#     def get_name(self):
#         print('123')
#         # self.name_.dismiss()

class CharCreate(Screen):
    name_input = ObjectProperty(None)
    name_pop = ObjectProperty(None)
    race_ = ObjectProperty(None)
    # class_ = ObjectProperty(None)

    _name = ''
    race = ''
    class_ = ''

    def get_name(self, input_name):
        CharCreate._name = input_name
        self.name_pop.dismiss()

    def disp(self):
        pprint([CharCreate._name, self.race, self.class_])


class ClassChoice(Screen):
    def btn(self, btn_text):
        CharCreate.class_ = btn_text


class RaceChoice(Screen):
    def btn(self, btn_text):
        CharCreate.race = btn_text


for i in {'Elf', 'Human', 'Gnome', 'Dwarf', 'Dragonborn', 'Half_orc', 'Tiefling', 'Aaracokra'}:
    setattr(RaceChoice, f"{i}", ObjectProperty(None))

for i in {'Barbarian', 'Monk', 'Rogue', 'Ranger', 'Wizard', 'Sorcerer', 'Cleric', 'Paladin'}:
    setattr(ClassChoice, f"{i}", ObjectProperty(None))


class InitRoll(Screen):

    def getcolumns(self):
        self.c1, self.c2 = init_roll.init_stat_roll()
        mega_grid = ObjectProperty()
        prime_grid = ObjectProperty()
        stat_col = ObjectProperty()
        input_col = ObjectProperty()
        checkbox = ObjectProperty()
        col1 = ObjectProperty()
        col2 = ObjectProperty()

        self.input_col.bind(on_text_validate=self.getname)
        self.mega_grid.add_widget(Button(text='Allocate', size_hint_y=None, height=100))

        for i, (stat, n1, n2) in enumerate(zip(STATS, self.c1, self.c2)):
            self.stat_col.add_widget(Label(id=f"{stat}",
                                           text=f"{stat}",
                                           color=(0, 1, 1, 1))
                                     )

            txtinput = TextInput(id=f"inp{i}", multiline=False)
            txtinput.bind(on_text_validate=self.getname)
            self.input_col.add_widget(txtinput)

            check = CheckBox(id=f"check{i}")
            self.checkbox.add_widget(check)

            self.col1.add_widget(Button(id=f"r{i}c3",
                                        text=f"{n1}")
                                 )

            self.col2.add_widget(Button(id=f"r{i}c4",
                                        text=f"{n2}")
                                 )

    def getname(self, txtinput):
        pprint([txtinput.id, txtinput.text])
        try:
            if int(txtinput.text) in self.c1 + self.c2:
                self.checkbox.children[5 - int(txtinput.id[-1])].active = True
        except ValueError:
            pass
        else:
            if all([child.active for child in self.checkbox.children]):
                pass
            else:
                txtinput.text = ''
