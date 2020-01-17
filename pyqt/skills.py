from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from pyqt.classes import CLASSES

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


class SkillInterface(QDialog):
    def __init__(self, skills=SKILLS.keys(), prompt='', rep=1):
        super().__init__()

        self.choice = []
        self.rep = rep
        self.skills = skills

        self.resize(600, 600)
        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 20, 500, 500))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        # self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_4.setObjectName(u"pushButton_4")
        #
        # self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        #
        # self.pushButton_8 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_8.setObjectName(u"pushButton_8")
        #
        # self.gridLayout.addWidget(self.pushButton_8, 3, 1, 1, 1)
        #
        # self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_3.setObjectName(u"pushButton_3")
        #
        # self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)
        #
        # self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_6.setObjectName(u"pushButton_6")
        #
        # self.gridLayout.addWidget(self.pushButton_6, 2, 0, 1, 1)
        #
        # self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_5.setObjectName(u"pushButton_5")
        #
        # self.gridLayout.addWidget(self.pushButton_5, 0, 0, 1, 1)
        #
        # self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_2.setObjectName(u"pushButton_2")
        #
        # self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        #
        # self.pushButton = QPushButton(self.gridLayoutWidget)
        # self.pushButton.setObjectName(u"pushButton")
        #
        # self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        #
        # self.pushButton_7 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_7.setObjectName(u"pushButton_7")
        #
        # self.gridLayout.addWidget(self.pushButton_7, 3, 0, 1, 1)
        #
        # self.pushButton_9 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_9.setObjectName(u"pushButton_9")
        #
        # self.gridLayout.addWidget(self.pushButton_9, 4, 0, 1, 1)
        #
        # self.pushButton_10 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_10.setObjectName(u"pushButton_10")
        #
        # self.gridLayout.addWidget(self.pushButton_10, 4, 1, 1, 1)

        for skill in self.skills:
            t = QPushButton(self.gridLayoutWidget)
            t.setObjectName(f"{skill}button")
            t.setText(f"{skill}")
            t.pressed.connect(self.return_choice)
            self.gridLayout.addWidget(t)

        #
        # self.pushButton.pressed.connect(self.return_choice)
        # self.pushButton_2.pressed.connect(self.return_choice)
        # self.pushButton_3.pressed.connect(self.return_choice)
        # self.pushButton_4.pressed.connect(self.return_choice)
        # self.pushButton_5.pressed.connect(self.return_choice)
        # self.pushButton_6.pressed.connect(self.return_choice)
        # self.pushButton_7.pressed.connect(self.return_choice)
        # self.pushButton_8.pressed.connect(self.return_choice)
        # self.pushButton_9.pressed.connect(self.return_choice)
        # self.pushButton_10.pressed.connect(self.return_choice)

        self.counter = 0

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
        self.exec_()

    def return_choice(self):
        self.choice.append(self.sender().text())
        self.sender().setEnabled(False)
        self.counter += 1
        if self.counter == self.rep:
            self.close()


    def retranslateUi(self, SkillInterface):
        SkillInterface.setWindowTitle(QCoreApplication.translate("RaceInterface", u"Dialog", None))
        # self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"dwarf", None))
        # self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"tiefling", None))
        # self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"halfling", None))
        # self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"gnome", None))
        # self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Human", None))
        # self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Elf", None))
        # self.pushButton.setText(QCoreApplication.translate("Dialog", u"Half-orc", None))
        # self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Dragonborn", None))
        # self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"Aaracokra", None))
        # self.pushButton_10.setText(QCoreApplication.translate("Dialog", u"Goliath", None))
    # retranslateUi



def set_skills(stats, class_):
    skill_choices = SkillInterface(skills=CLASSES[class_]['skill_prof']['skills'],
                                   prompt= f"choose {CLASSES[class_]['skill_prof']['num']} from\n"
                                           f"{CLASSES[class_]['skill_prof']['skills']}).choice",
                                   rep=2).choice

    char_skill_score_stat = {skill: {'score': stats[skill_score_stat['stat']]['mod'],
                                     'stat': skill_score_stat['stat'],
                                     'prof': False}
                             for skill, skill_score_stat in SKILLS.items()}

    for skill in skill_choices:
        char_skill_score_stat[skill]['score'] += 2
        char_skill_score_stat[skill]['prof'] = True
        print(char_skill_score_stat)

    return char_skill_score_stat
