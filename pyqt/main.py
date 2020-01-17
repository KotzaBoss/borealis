import sys
from os.path import dirname

TOP_DIR = dirname(__file__)
sys.path.append(dirname(__file__))

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pyqt.new_characters import CharacterCreation

STATS = {'str': {'score': 0, 'mod': 0, 'save': {'score': 0, 'prof': False}},
         'dex': {'score': 0, 'mod': 0, 'save': {'score': 0, 'prof': False}},
         'con': {'score': 0, 'mod': 0, 'save': {'score': 0, 'prof': False}},
         'int': {'score': 0, 'mod': 0, 'save': {'score': 0, 'prof': False}},
         'wis': {'score': 0, 'mod': 0, 'save': {'score': 0, 'prof': False}},
         'cha': {'score': 0, 'mod': 0, 'save': {'score': 0, 'prof': False}}
         }


class Borealis(QMainWindow):

    def __init__(self):
        super().__init__()

        font = QFont()
        font.setFamily("mononoki")

        self.setFont(font)
        self.resize(700, 500)
        self.setWindowTitle('Borealis')

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        # --- ACTIVE CHAR
        self.active_char_label = QLabel(self.centralWidget)
        self.active_char_label.setGeometry(QRect(450, 10, 209, 16))
        self.active_char_label.setFont(font)
        self.active_char_label.setText('Active Character')

        self.actcharwin = QTextBrowser(self.centralWidget)
        self.actcharwin.setGeometry(QRect(450, 30, 211, 291))
        # ---

        # --- MEMORY WIN
        self.memwin_label = QLabel(self.centralWidget)
        self.memwin_label.setGeometry(QRect(10, 10, 209, 16))
        self.memwin_label.setFont(font)
        self.memwin_label.setText('Main')

        self.memwin = QTextBrowser(self.centralWidget)
        self.memwin.setGeometry(QRect(10, 30, 431, 291))
        # ---

        # --- CMDLINE
        self.cmdline = QLineEdit(self.centralWidget)
        self.cmdline.setGeometry(QRect(10, 330, 651, 28))
        self.cmdline.setFont(font)

        self.cmdline.returnPressed.connect(self.run_cmd)
        # ---

        #  --- ERROR WIN
        self.errwin = QTextBrowser(self.centralWidget)
        self.errwin.setGeometry(QRect(10, 370, 651, 96))
        #  ---

        self.active_char_label.raise_()
        self.memwin_label.raise_()
        self.cmdline.raise_()
        self.actcharwin.raise_()
        self.cmdline.raise_()
        self.errwin.raise_()
        self.memwin.raise_()

        Borealis._char_create = CharacterCreation()
        COMMANDS.update({'new': {'func': Borealis._char_create.create_character}})

    def run_cmd(self):
        if self.cmdline.text() in COMMANDS.keys():
            COMMANDS[self.cmdline.text()]['func']()
        else:
            self.errwin.setText(
                "{new}: Command not found\n{old}".format(old=self.errwin.toPlainText(), new=self.cmdline.text()))
        self.cmdline.clear()



def main():
    import sys
    app = QApplication(sys.argv)
    mainwin = Borealis()
    mainwin.show()
    sys.exit(app.exec_())


COMMANDS = {'new': {'func': '', 'help': 'New character'},
            'read': {'func': 'read_character', 'help': 'Read from character'},
            'delete': {'func': 'delete_character', 'help': 'Delete character'},
            'show': {'func': 'show_character', 'help': 'Display a character'},
            'roll': {'func': 'dice_roller', 'help': 'Roll dy die, x times'},
            'init': {'func': 'init_stat_roll', 'help': 'Roll two columns of character creaton stats'},
            'exit': {'func': 'Shell.rmv_credit', 'help': 'Self explanatory'},
            'help': {'func': 'help_', 'help': "Type 'help <command>' to get more information"}
            }

if __name__ == '__main__':
    main()
