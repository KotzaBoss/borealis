import json

from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager

from __kivy.character import CharCreate, CHARACTERS


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.textin = ObjectProperty()

    def display(self):
        if CHARACTERS:
            for name, char in CHARACTERS.items():
                with open(f'char_storage/{name}.json', 'r') as f:
                    json_ = json.load(f)
                    json_ = json.dumps(json_, indent=8)
                    self.textin.text = str(json_)
                    self.textin.text += '\n-----------------\n'

        else:
            self.textin.text = 'error'


class ToolBar(Screen):
    pass


class WindowManager(ScreenManager):
    charcreate = CharCreate()
    main = MainWindow()
    pass
