"""
WEAPONS = 'daggers':
               {'att': 10,
               'dmg': '1d4',
               'comment': 'lawful targets take +1d6 phycic dmg',
               'unique': (add_to_dmg, '1d6')
                }
           }
"""

WEAPONS = {'stick': {'att': 2, 'dmg': '1d4'}}


def new_weapon():
    print(f"Give new _weapon stats")
    name = input(f"Weapon Name: ")
    att = input(f"Attack Bonus: ")
    dmg = input(f"Damage Dice: ")
    comment = input(f"Comment: ")
    unique = input(f"Unique: ")

    WEAPONS[name] = {'att': att, 'dmg': dmg, 'comment': comment, 'unique': unique}


def create(thing):
    new = {'item': '', '_weapon': new_weapon}

    if thing in new.keys():
        new[thing]()


def loop():
    credit = True

    while credit:
        print(WEAPONS)
        thing = input('new: ')
        create(thing)
        print(WEAPONS)
        credit = False
