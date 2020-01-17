from PyQt5 import QtWidgets


class Win(object):
    memwin = None
    errwin = None
    cmdline = None
    char_create = None


class MultiWindows(QtWidgets.QMainWindow):

    def __init__(self):
        self.__windows = []

    def addwindow(self, window):
        self.__windows.append(window)

    def show_only(self, win):
        for window in self.__windows:
            if window == win:
                win.show()
                break

    def show(self):
        for current_child_window in self.__windows:
            current_child_window.show()
