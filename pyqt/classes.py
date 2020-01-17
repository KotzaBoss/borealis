import random as rnd

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from .armors import LIGHT_ARMORS, NO_ARMOR
from .weapons import WEAPONS

rnd.seed(666)

CLASSES = {'ranger': {'init_hp': 10 + rnd.randint(1, 10),
                      'hit_dice': '1d10',
                      'lvlup_mod': 'con',
                      'hp_incr': '1d10',
                      'saves': ('str', 'dex'),
                      'skill_prof': {'skills': {'animal handling',
                                                'athletics',
                                                'insight',
                                                'investigation',
                                                'nature',
                                                'perception',
                                                'stealth',
                                                'survival'},
                                     'num': 2
                                     },
                      'armor': LIGHT_ARMORS['leather'],
                      'lvls': {1: {'prof': 2,
                                   'features': {
                                       'favored enemy': {'descr': 'choose enemy, learn their language if they have one',
                                                         'fx': 'adv to wis, int checks on favored enemy'},
                                       'natural explorer': {
                                           'descr': 'choose terain int, wis checks on it are calced with 2*prof',
                                           'fx': "Difficult terrain doesn’t slow your group’s travel.\n"
                                                 "Your group can’t become lost except by magical means.\n"
                                                 "Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.\n"
                                                 "If you are traveling alone, you can move stealthily at a normal pace.\n"
                                                 "When you forage, you find twice as much food as you normally would.\n"
                                                 "While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area."}
                                   }
                                   }
                               }
                      },
           'barbarian': {'init_hp': 12 + rnd.randint(1, 12),
                         'hit_dice': '1d12',
                         'lvlup_mod': 'con',
                         'hp_incr': '1d12',
                         'saves': ('str', 'con'),
                         'skill_prof': {'skills': {'animal handling',
                                                   'athletics',
                                                   'intimidation',
                                                   'nature',
                                                   'perception',
                                                   'survival'},
                                        'armor': ('light armor',
                                                  'medium armor',
                                                  'shields'),
                                        'weapons': ('simple weapons',
                                                    'martial weapons'),
                                        'num': 2
                                        },
                         'armor': NO_ARMOR,
                         'weapons': (WEAPONS['greataxe'], WEAPONS['shortsword']),
                         'lvls': {1: {'prof': 2,
                                      'features': {'rage': {
                                          'descr': 'You have advantage on Strength checks and Strength saving throws.\n'
                                                   'When you make a melee _weapon attack_roll using Strength, you gain a bonus to the damage_roll roll that increases as you gain levels as a barbarian, as shown in the Rage Damage column of the Barbarian table.'
                                                   'You have resistance to bludgeoning, piercing, and slashing damage_roll.'},
                                          'unarmored defense': {
                                              'descr': 'While you are not wearing any armor, your Armor Class equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit.',
                                          }
                                      }
                                      }
                                  }
                         }

           }


class ClassInterface(QDialog):
    def __init__(self):
        super().__init__()

        self.choice = None

        self.resize(400, 300)
        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 20, 361, 261))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 2, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 3, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 4, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 4, 1, 1, 1)


        self.pushButton.pressed.connect(self.return_choice)
        self.pushButton_2.pressed.connect(self.return_choice)
        self.pushButton_3.pressed.connect(self.return_choice)
        self.pushButton_4.pressed.connect(self.return_choice)
        self.pushButton_5.pressed.connect(self.return_choice)
        self.pushButton_6.pressed.connect(self.return_choice)
        self.pushButton_7.pressed.connect(self.return_choice)
        self.pushButton_8.pressed.connect(self.return_choice)
        self.pushButton_9.pressed.connect(self.return_choice)
        self.pushButton_10.pressed.connect(self.return_choice)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
        self.exec_()

    def return_choice(self):
        self.close()
        self.choice = self.sender().text()


    def retranslateUi(self, ClassInterface):
        ClassInterface.setWindowTitle(QCoreApplication.translate("RaceInterface", u"Dialog", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"barbarian", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"rogue", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"bard", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"monk", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"ranger", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"wizard", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"sorcerer", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"druid", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"cleric", None))
        self.pushButton_10.setText(QCoreApplication.translate("Dialog", u"fighter", None))
    # retranslateUi