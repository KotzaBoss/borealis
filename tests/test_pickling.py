import os
import pickle

from character import Character
from overlord import Azathoth

testf_dir = os.path.dirname(__file__) + '/test.pickle'


def test_pickling():
    ch = Character()
    with open(testf_dir, 'wb') as f:
        pickle.dump(ch, f)
    with open(testf_dir, 'rb') as f:
        read_ch = pickle.load(f)
    Azathoth.load_storage(read_ch)

    assert ch == read_ch
