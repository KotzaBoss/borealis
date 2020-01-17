"""
>>> RACE = {'race': {'stats': {'str': 1,  # <-- will be added during char
>>>                            'dex': 1,  #     creation
>>>                            'con': 1,
>>>                            'int': 1,
>>>                            'wis': 1,
>>>                            'cha': 1
>>>                            },
>>>                    'size': 'medium',
>>>                    'speed': 30,
>>>                    'resistance': 'poison'
>>>                    },
"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

RACES = {'human': {'stats': {'str': 1,
                             'dex': 1,
                             'con': 1,
                             'int': 1,
                             'wis': 1,
                             'cha': 1
                             },
                   'size': 'medium',
                   'speed': 30,
                   'resistance': None,
                   'prof': None
                   },
         'dwarf': {'stats': {'str': 0,
                             'dex': 0,
                             'con': 2,
                             'int': 0,
                             'wis': 0,
                             'cha': 0},
                   'size': 'medium',
                   'speed': 25,
                   'damage': {'resist': 'poison',
                              'immune': None,
                              'vulnerable': None,
                              },
                   'prof': {'smith’s tools',
                            'brewer’s supplies',
                            'mason’s tools'}
                   }
         }

class RaceInterface(QDialog):
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


    def retranslateUi(self, RaceInterface):
        RaceInterface.setWindowTitle(QCoreApplication.translate("RaceInterface", u"Dialog", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"dwarf", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"tiefling", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"halfling", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"gnome", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Human", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Elf", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Half-orc", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Dragonborn", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"Aaracokra", None))
        self.pushButton_10.setText(QCoreApplication.translate("Dialog", u"Goliath", None))
    # retranslateUi