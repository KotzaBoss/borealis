from kivy.app import App
from kivy.lang import Builder

from __kivy.winmanagement import WindowManager

Builder.load_file('racechoice.kv')
Builder.load_file('classchoice.kv')
Builder.load_file('initroll.kv')
Builder.load_file('design.kv')


class MainApp(App):

    # for i in {'Elf', '\
    def build(self):
        return WindowManager()


# ------------------------
if __name__ == '__main__':
    MainApp().run()
