import pickle

from character import Character
from overlord import Azathoth


def test_pickling():
    ch = Character()
    with open('test.pickle', 'wb') as f:
        pickle.dump(ch, f)
    with open("test.pickle", 'rb') as f:
        read_ch = pickle.load(f)
    Azathoth.load_storage(read_ch)

    assert ch == read_ch
