from Item.Components.ac import AC
from Item.Components.armortype import ArmorType
from Item.Components.item import Item
from Item.Components.weight import Weight

if __name__ == '__main__':
    item = Item()
    item.insert_component(
        AC(13, 10, 5, True),
        Weight(),
        ArmorType(),
    )
    print(item)
