from kivy.uix.screenmanager import Screen, ScreenManager

from __kivy.character_creation import CharCreate


class WindowManager(ScreenManager):
    charcreate = CharCreate()
    pass


class MainWindow(Screen):
    pass
