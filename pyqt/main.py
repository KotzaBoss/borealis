import sys
from os.path import dirname

TOP_DIR = dirname(__file__)
sys.path.append(dirname(__file__))

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import re
from pyqt.utils import init_stat_roll, finalise_init
from pyqt.classes import CLASSES
import json
import os
from pyqt.races import RACES

STATS = {'str': {'score': 0, 'mod': 0, 'save': {'score': 0, 'prof': False}},
         'dex': {'score': 0, 'mod': 0, 'save': {'score': 0, 'prof': False}},
         'con': {'score': 0, 'mod': 0, 'save': {'score': 0, 'prof': False}},
         'int': {'score': 0, 'mod': 0, 'save': {'score': 0, 'prof': False}},
         'wis': {'score': 0, 'mod': 0, 'save': {'score': 0, 'prof': False}},
         'cha': {'score': 0, 'mod': 0, 'save': {'score': 0, 'prof': False}}
         }


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


class CharacterCreation(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setObjectName("CharacterCreation")
        self.resize(564, 521)

        # STAT LINEDIT AND INDICATOR
        self.horizontalLayoutWidget = QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QRect(30, 60, 160, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.str_lay = QHBoxLayout(self.horizontalLayoutWidget)
        self.str_lay.setContentsMargins(0, 0, 0, 0)
        self.str_lay.setObjectName("str_lay")
        self.str = QLabel(self.horizontalLayoutWidget)
        font = QFont()
        font.setFamily("mononoki")
        self.str.setFont(font)
        self.str.setAlignment(Qt.AlignCenter)
        self.str.setObjectName("str")
        self.str_lay.addWidget(self.str)
        self.str_in = QLineEdit(self.horizontalLayoutWidget)
        self.str_in.setObjectName("str_in")
        self.str_lay.addWidget(self.str_in)
        self.str_ind = QLabel(self.horizontalLayoutWidget)
        font = QFont()
        font.setFamily("mononoki")
        self.str_ind.setFont(font)
        self.str_ind.setObjectName("str_ind")
        self.str_lay.addWidget(self.str_ind)
        self.horizontalLayoutWidget_2 = QWidget(self)
        self.horizontalLayoutWidget_2.setGeometry(QRect(30, 100, 160, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.dex_lay = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.dex_lay.setContentsMargins(0, 0, 0, 0)
        self.dex_lay.setObjectName("dex_lay")
        self.dex = QLabel(self.horizontalLayoutWidget_2)
        font = QFont()
        font.setFamily("mononoki")
        self.dex.setFont(font)
        self.dex.setAlignment(Qt.AlignCenter)
        self.dex.setObjectName("dex")
        self.dex_lay.addWidget(self.dex)
        self.dex_in = QLineEdit(self.horizontalLayoutWidget_2)
        self.dex_in.setObjectName("dex_in")
        self.dex_lay.addWidget(self.dex_in)
        self.dex_ind = QLabel(self.horizontalLayoutWidget_2)
        font = QFont()
        font.setFamily("mononoki")
        self.dex_ind.setFont(font)
        self.dex_ind.setObjectName("dex_ind")
        self.dex_lay.addWidget(self.dex_ind)
        self.horizontalLayoutWidget_3 = QWidget(self)
        self.horizontalLayoutWidget_3.setGeometry(QRect(30, 140, 160, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.con_lay = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.con_lay.setContentsMargins(0, 0, 0, 0)
        self.con_lay.setObjectName("con_lay")
        self.con = QLabel(self.horizontalLayoutWidget_3)
        font = QFont()
        font.setFamily("mononoki")
        self.con.setFont(font)
        self.con.setAlignment(Qt.AlignCenter)
        self.con.setObjectName("con")
        self.con_lay.addWidget(self.con)
        self.con_in = QLineEdit(self.horizontalLayoutWidget_3)
        font = QFont()
        font.setFamily("mononoki")
        self.con_in.setFont(font)
        self.con_in.setObjectName("con_in")
        self.con_lay.addWidget(self.con_in)
        self.con_ind = QLabel(self.horizontalLayoutWidget_3)
        font = QFont()
        font.setFamily("mononoki")
        self.con_ind.setFont(font)
        self.con_ind.setObjectName("con_ind")
        self.con_lay.addWidget(self.con_ind)
        self.horizontalLayoutWidget_4 = QWidget(self)
        self.horizontalLayoutWidget_4.setGeometry(QRect(30, 180, 160, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.int_lay = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.int_lay.setContentsMargins(0, 0, 0, 0)
        self.int_lay.setObjectName("int_lay")
        self.int_2 = QLabel(self.horizontalLayoutWidget_4)
        font = QFont()
        font.setFamily("mononoki")
        self.int_2.setFont(font)
        self.int_2.setAlignment(Qt.AlignCenter)
        self.int_2.setObjectName("int_2")
        self.int_lay.addWidget(self.int_2)
        self.int_in = QLineEdit(self.horizontalLayoutWidget_4)
        font = QFont()
        font.setFamily("mononoki")
        self.int_in.setFont(font)
        self.int_in.setObjectName("int_in")
        self.int_lay.addWidget(self.int_in)
        self.int_ind = QLabel(self.horizontalLayoutWidget_4)
        font = QFont()
        font.setFamily("mononoki")
        self.int_ind.setFont(font)
        self.int_ind.setObjectName("int_ind")
        self.int_lay.addWidget(self.int_ind)
        self.horizontalLayoutWidget_5 = QWidget(self)
        self.horizontalLayoutWidget_5.setGeometry(QRect(30, 220, 160, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.wis_lay = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.wis_lay.setContentsMargins(0, 0, 0, 0)
        self.wis_lay.setObjectName("wis_lay")
        self.wis = QLabel(self.horizontalLayoutWidget_5)
        font = QFont()
        font.setFamily("mononoki")
        self.wis.setFont(font)
        self.wis.setAlignment(Qt.AlignCenter)
        self.wis.setObjectName("wis")
        self.wis_lay.addWidget(self.wis)
        self.wis_in = QLineEdit(self.horizontalLayoutWidget_5)
        font = QFont()
        font.setFamily("mononoki")
        self.wis_in.setFont(font)
        self.wis_in.setObjectName("wis_in")
        self.wis_lay.addWidget(self.wis_in)
        self.wis_ind = QLabel(self.horizontalLayoutWidget_5)
        font = QFont()
        font.setFamily("mononoki")
        self.wis_ind.setFont(font)
        self.wis_ind.setObjectName("wis_ind")
        self.wis_lay.addWidget(self.wis_ind)
        self.horizontalLayoutWidget_6 = QWidget(self)
        self.horizontalLayoutWidget_6.setGeometry(QRect(30, 260, 160, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.cha_lay = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.cha_lay.setContentsMargins(0, 0, 0, 0)
        self.cha_lay.setObjectName("cha_lay")
        self.cha = QLabel(self.horizontalLayoutWidget_6)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cha.sizePolicy().hasHeightForWidth())
        self.cha.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("mononoki")
        self.cha.setFont(font)
        self.cha.setAlignment(Qt.AlignCenter)
        self.cha.setObjectName("cha")
        self.cha_lay.addWidget(self.cha)
        self.cha_in = QLineEdit(self.horizontalLayoutWidget_6)
        font = QFont()
        font.setFamily("mononoki")
        self.cha_in.setFont(font)
        self.cha_in.setObjectName("cha_in")
        self.cha_lay.addWidget(self.cha_in)
        self.cha_ind = QLabel(self.horizontalLayoutWidget_6)
        font = QFont()
        font.setFamily("mononoki")
        self.cha_ind.setFont(font)
        self.cha_ind.setObjectName("cha_ind")
        self.cha_lay.addWidget(self.cha_ind)

        # COLUMNS AND COL_LABELS
        self.horizontalLayoutWidget_7 = QWidget(self)
        self.horizontalLayoutWidget_7.setGeometry(QRect(210, 60, 181, 41))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.hor_lay_row1 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.hor_lay_row1.setContentsMargins(0, 0, 0, 0)
        self.hor_lay_row1.setObjectName("hor_lay_row1")
        self.col01 = QLabel(self.horizontalLayoutWidget_7)
        self.col01font = QFont()
        self.col01font.setFamily("mononoki")
        self.col01.setFont(self.col01font)
        self.col01.setAlignment(Qt.AlignCenter)
        self.col01.setObjectName("col01")
        self.hor_lay_row1.addWidget(self.col01)
        self.row1_sep = QFrame(self.horizontalLayoutWidget_7)
        self.row1_sep.setFrameShape(QFrame.VLine)
        self.row1_sep.setFrameShadow(QFrame.Sunken)
        self.row1_sep.setObjectName("row1_sep")
        self.hor_lay_row1.addWidget(self.row1_sep)
        self.col02 = QLabel(self.horizontalLayoutWidget_7)
        self.coll12font = QFont()
        self.coll12font.setFamily("mononoki")
        self.col02.setFont(self.coll12font)
        self.col02.setAlignment(Qt.AlignCenter)
        self.col02.setObjectName("col02")
        self.hor_lay_row1.addWidget(self.col02)
        self.horizontalLayoutWidget_8 = QWidget(self)
        self.horizontalLayoutWidget_8.setGeometry(QRect(210, 100, 181, 41))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.hor_lay_row2 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.hor_lay_row2.setContentsMargins(0, 0, 0, 0)
        self.hor_lay_row2.setObjectName("hor_lay_row2")
        self.col11 = QLabel(self.horizontalLayoutWidget_8)
        self.col11font = QFont()
        self.col11font.setFamily("mononoki")
        self.col11.setFont(self.col11font)
        self.col11.setAlignment(Qt.AlignCenter)
        self.col11.setObjectName("col11")
        self.hor_lay_row2.addWidget(self.col11)
        self.row2_sep = QFrame(self.horizontalLayoutWidget_8)
        self.row2_sep.setFrameShape(QFrame.VLine)
        self.row2_sep.setFrameShadow(QFrame.Sunken)
        self.row2_sep.setObjectName("row2_sep")
        self.hor_lay_row2.addWidget(self.row2_sep)
        self.col12 = QLabel(self.horizontalLayoutWidget_8)
        self.col12font = QFont()
        self.col12font.setFamily("mononoki")
        self.col12.setFont(self.col12font)
        self.col12.setAlignment(Qt.AlignCenter)
        self.col12.setObjectName("col12")
        self.hor_lay_row2.addWidget(self.col12)
        self.horizontalLayoutWidget_9 = QWidget(self)
        self.horizontalLayoutWidget_9.setGeometry(QRect(210, 140, 181, 41))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.hor_lay_row3 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.hor_lay_row3.setContentsMargins(0, 0, 0, 0)
        self.hor_lay_row3.setObjectName("hor_lay_row3")
        self.col21 = QLabel(self.horizontalLayoutWidget_9)
        self.col21font = QFont()
        self.col21font.setFamily("mononoki")
        self.col21.setFont(self.col21font)
        self.col21.setAlignment(Qt.AlignCenter)
        self.col21.setObjectName("col21")
        self.hor_lay_row3.addWidget(self.col21)
        self.row3_sep = QFrame(self.horizontalLayoutWidget_9)
        self.row3_sep.setFrameShape(QFrame.VLine)
        self.row3_sep.setFrameShadow(QFrame.Sunken)
        self.row3_sep.setObjectName("row3_sep")
        self.hor_lay_row3.addWidget(self.row3_sep)
        self.col22 = QLabel(self.horizontalLayoutWidget_9)
        self.col22font = QFont()
        self.col22font.setFamily("mononoki")
        self.col22.setFont(self.col22font)
        self.col22.setAlignment(Qt.AlignCenter)
        self.col22.setObjectName("col22")
        self.hor_lay_row3.addWidget(self.col22)
        self.horizontalLayoutWidget_10 = QWidget(self)
        self.horizontalLayoutWidget_10.setGeometry(QRect(210, 180, 181, 41))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.hor_lay_row4 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.hor_lay_row4.setContentsMargins(0, 0, 0, 0)
        self.hor_lay_row4.setObjectName("hor_lay_row4")
        self.col31 = QLabel(self.horizontalLayoutWidget_10)
        self.col31font = QFont()
        self.col31font.setFamily("mononoki")
        self.col31.setFont(self.col31font)
        self.col31.setAlignment(Qt.AlignCenter)
        self.col31.setObjectName("col31")
        self.hor_lay_row4.addWidget(self.col31)
        self.row4_sep = QFrame(self.horizontalLayoutWidget_10)
        self.row4_sep.setFrameShape(QFrame.VLine)
        self.row4_sep.setFrameShadow(QFrame.Sunken)
        self.row4_sep.setObjectName("row4_sep")
        self.hor_lay_row4.addWidget(self.row4_sep)
        self.col32 = QLabel(self.horizontalLayoutWidget_10)
        self.col32font = QFont()
        self.col32font.setFamily("mononoki")
        self.col32.setFont(self.col32font)
        self.col32.setAlignment(Qt.AlignCenter)
        self.col32.setObjectName("col32")
        self.hor_lay_row4.addWidget(self.col32)
        self.horizontalLayoutWidget_11 = QWidget(self)
        self.horizontalLayoutWidget_11.setGeometry(QRect(210, 220, 181, 41))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.hor_lay_row5 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.hor_lay_row5.setContentsMargins(0, 0, 0, 0)
        self.hor_lay_row5.setObjectName("hor_lay_row5")
        self.col41 = QLabel(self.horizontalLayoutWidget_11)
        self.col41font = QFont()
        self.col41font.setFamily("mononoki")
        self.col41.setFont(self.col41font)
        self.col41.setAlignment(Qt.AlignCenter)
        self.col41.setObjectName("col41")
        self.hor_lay_row5.addWidget(self.col41)
        self.row5_sep = QFrame(self.horizontalLayoutWidget_11)
        self.row5_sep.setFrameShape(QFrame.VLine)
        self.row5_sep.setFrameShadow(QFrame.Sunken)
        self.row5_sep.setObjectName("row5_sep")
        self.hor_lay_row5.addWidget(self.row5_sep)
        self.col42 = QLabel(self.horizontalLayoutWidget_11)
        self.col42font = QFont()
        self.col42font.setFamily("mononoki")
        self.col42.setFont(self.col42font)
        self.col42.setAlignment(Qt.AlignCenter)
        self.col42.setObjectName("col42")
        self.hor_lay_row5.addWidget(self.col42)
        self.horizontalLayoutWidget_12 = QWidget(self)
        self.horizontalLayoutWidget_12.setGeometry(QRect(210, 260, 181, 41))
        self.horizontalLayoutWidget_12.setObjectName("horizontalLayoutWidget_12")
        self.hor_lay_row6 = QHBoxLayout(self.horizontalLayoutWidget_12)
        self.hor_lay_row6.setContentsMargins(0, 0, 0, 0)
        self.hor_lay_row6.setObjectName("hor_lay_row6")
        self.col51 = QLabel(self.horizontalLayoutWidget_12)
        self.col51font = QFont()
        self.col51font.setFamily("mononoki")
        self.col51.setFont(self.col51font)
        self.col51.setAlignment(Qt.AlignCenter)
        self.col51.setObjectName("col51")
        self.hor_lay_row6.addWidget(self.col51)
        self.row6_sep = QFrame(self.horizontalLayoutWidget_12)
        self.row6_sep.setFrameShape(QFrame.VLine)
        self.row6_sep.setFrameShadow(QFrame.Sunken)
        self.row6_sep.setObjectName("row6_sep")
        self.hor_lay_row6.addWidget(self.row6_sep)
        self.col52 = QLabel(self.horizontalLayoutWidget_12)
        self.col52font = QFont()
        self.col52font.setFamily("mononoki")
        self.col52.setFont(self.col52font)
        self.col52.setAlignment(Qt.AlignCenter)
        self.col52.setObjectName("col52")
        self.hor_lay_row6.addWidget(self.col52)
        self.horizontalLayoutWidget_13 = QWidget(self)
        self.horizontalLayoutWidget_13.setGeometry(QRect(210, 20, 181, 41))
        self.horizontalLayoutWidget_13.setObjectName("horizontalLayoutWidget_13")
        self.hor_lay_header = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.hor_lay_header.setContentsMargins(0, 0, 0, 0)
        self.hor_lay_header.setObjectName("hor_lay_header")
        self.c1_header = QLabel(self.horizontalLayoutWidget_13)
        font = QFont()
        font.setFamily("mononoki")
        self.c1_header.setFont(font)
        self.c1_header.setAlignment(Qt.AlignCenter)
        self.c1_header.setObjectName("c1_header")
        self.hor_lay_header.addWidget(self.c1_header)
        self.line_8 = QFrame(self.horizontalLayoutWidget_13)
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.hor_lay_header.addWidget(self.line_8)
        self.c2_header = QLabel(self.horizontalLayoutWidget_13)
        font = QFont()
        font.setFamily("mononoki")
        self.c2_header.setFont(font)
        self.c2_header.setAlignment(Qt.AlignCenter)
        self.c2_header.setObjectName("c2_header")
        self.hor_lay_header.addWidget(self.c2_header)

        # CONNECT LINEDITS TO VALIDATION FUNCTION
        self.str_in.textEdited.connect(self.validate_input)
        self.dex_in.textEdited.connect(self.validate_input)
        self.con_in.textEdited.connect(self.validate_input)
        self.int_in.textEdited.connect(self.validate_input)
        self.wis_in.textEdited.connect(self.validate_input)
        self.cha_in.textEdited.connect(self.validate_input)

        # ALLOCATE BUTTON
        self.allocate = QPushButton(self)
        self.allocate.setObjectName(u"allocate")
        self.allocate.setGeometry(QRect(30, 320, 111, 41))
        self.allocate.setFont(font)
        self.allocate.setText('Allocate')
        self.allocate.setEnabled(False)
        self.allocate.pressed.connect(self.finalise)

        # Keeping things together
        self.stat_indicators = {self.str_ind, self.dex_ind, self.con_ind, self.int_ind, self.wis_ind, self.cha_ind}

        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, CharacterCreation):
        _translate = QCoreApplication.translate
        CharacterCreation.setWindowTitle(_translate("CharacterCreation", "Form"))
        self.str.setText(_translate("CharacterCreation", "STR"))
        self.str_ind.setText(_translate("CharacterCreation", "-"))
        self.dex.setText(_translate("CharacterCreation", "DEX"))
        self.dex_ind.setText(_translate("CharacterCreation", "-"))
        self.con.setText(_translate("CharacterCreation", "CON"))
        self.con_ind.setText(_translate("CharacterCreation", "-"))
        self.int_2.setText(_translate("CharacterCreation", "INT"))
        self.int_ind.setText(_translate("CharacterCreation", "-"))
        self.wis.setText(_translate("CharacterCreation", "WIS"))
        self.wis_ind.setText(_translate("CharacterCreation", "-"))
        self.cha.setText(_translate("CharacterCreation", "CHA"))
        self.cha_ind.setText(_translate("CharacterCreation", "-"))

        self.c1_header.setText(_translate("CharacterCreation", "C1"))
        self.c2_header.setText(_translate("CharacterCreation", "C2"))

    def validate_input(self):
        in_text = self.sender().text()
        stat_ind = getattr(self, self.sender().objectName() + 'd')

        print(re.search(r"(\b\d\d\b)|(\b\d\b)", in_text))
        if not re.search(r"(\b\d\d\b)|(\b\d\b)", in_text):
            self.sender().clear()
            stat_ind.setText('X')
        else:
            try:
                if int(in_text) in self.c1 + self.c2:
                    stat_ind.setText('!')
                else:
                    stat_ind.setText('X')

            except ValueError as ve:
                print(ve)

        for stat_indicator in self.stat_indicators:
            if stat_indicator.text() != '!':
                return
        else:
            self.allocate.setEnabled(True)

    def set_skills(self, stats, class_):
        try:
            char_skill_score_stat = {skill: {'score': stats[skill_score_stat['stat']]['mod'],
                                             'stat': skill_score_stat['stat'],
                                             'prof': False}
                                     for skill, skill_score_stat in SKILLS.items()}

            for _ in range(CLASSES[class_]['skill_prof']['num']):
                skill = QInputDialog.getText(self, 'skills', f"choose {CLASSES[class_]['skill_prof']['num']} from\n"
                                                             f"{CLASSES[class_]['skill_prof']['skills']} with <enter>")[
                    0]
                while True:
                    print(skill, CLASSES[class_]['skill_prof']['skills'])
                    if skill in CLASSES[class_]['skill_prof']['skills']:
                        char_skill_score_stat[skill]['score'] += 2
                        char_skill_score_stat[skill]['prof'] = True
                        break
                    else:
                        skill = QInputDialog.getText(self, 'skills',
                                                     f"choose {CLASSES[class_]['skill_prof']['num']} from\n"
                                                     f"{CLASSES[class_]['skill_prof']['skills']} with <enter>\n"
                                                     f"skill not found")[0]
            else:
                return char_skill_score_stat
        except Exception as e:
            print(f"{e.__traceback__.tb_lineno} {e}")

    def create_character(self):
        """ Read name race class of character and throw initial rolls and skills and save character file """

        self.name = self.choose_name()
        self.race = self.choose_race(self.name)
        self.class_ = self.choose_class(self.name)
        self.c1, self.c2 = init_stat_roll(self.race, self.class_)
        for i, (n1, n2) in enumerate(zip(self.c1, self.c2)):
            getattr(self, "col{row}1".format(row=i)).setText(str(n1))
            getattr(self, "col{row}2".format(row=i)).setText(str(n2))
        self.show()

    def finalise(self):
        self.close()
        for stat in STATS:
            STATS[stat]['score'] = int(getattr(self, f"{stat}_in").text())
        init_stats = finalise_init(self.race, self.class_, STATS)
        print(init_stats)
        init_skills = self.set_skills(init_stats, self.class_)
        CHARACTERS[self.name] = Character(init=True, name=self.name, race=self.race, class_=self.class_,
                                          init_stats=init_stats, init_skills=init_skills)
        save_character(CHARACTERS[self.name])

    def choose_name(self):
        name = QInputDialog.getText(self, "Name", "What is your name?")
        print(name)
        return name[0]

    def choose_race(self, name):
        race = QInputDialog.getText(self, 'Race',
                                    f"What is {name}'{'' if name[-1] in ('s', 'S') else 's'} race: ")[0]
        while True:
            if race not in RACES:
                race = QInputDialog.getText(self, 'Race', 'Unavailable race try again')[0]
            else:
                return race

    def choose_class(self, name):
        class_ = QInputDialog.getText(self, 'Race',
                                      f"What is {name}'{'' if name[-1] in ('s', 'S') else 's'} class: ")[0]
        while True:
            if class_ not in CLASSES.keys():
                # class_ = cmdline_input(f"Unavailable class try again: ", prompt=False)
                class_ = QInputDialog.getText(self, 'Race', 'Unavailable class')[0]
            else:
                return class_


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


def init_hp(stats, class_):
    return {'max': CLASSES[class_]['init_hp'] + stats[CLASSES[class_]['lvlup_mod']]['mod'],
            'curr': CLASSES[class_]['init_hp'] + stats[CLASSES[class_]['lvlup_mod']]['mod'],
            'hit_dice': CLASSES[class_]['hit_dice'],
            'lvlup_mod': CLASSES[class_]['lvlup_mod']}


def save_character(character):
    """ Save character in json file """
    with open(os.path.join(TOP_DIR, f"char_storage/{character.name}.json"), 'w') as outfile:
        json.dump(character.__dict__,
                  outfile,
                  indent=10,
                  ensure_ascii=False
                  )


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
