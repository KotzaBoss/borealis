from item import Item
from roll import roll
def item_creation_test(components, name='Unamed Item'):
    item = Item(name=name, components=components)
    print(item)
    return item


def roll_test(xdy=''):
    for _xdy in xdy:
        print(f"{_xdy} -> {roll(_xdy)}")
