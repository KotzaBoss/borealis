from kivy.uix.screenmanager import Screen, ScreenManager

from __kivy.character_creation import CharCreate


class MainWindow(Screen):
    pass


class ToolBar(Screen):
    pass


class WindowManager(ScreenManager):
    charcreate = CharCreate()
    main = MainWindow()
    pass
