import os
import sys

sys.path.append(os.path.abspath(__file__ + "/../../"))  # 9000 IQ move

from overlord import Azathoth

CMDS = ['new', 'import', 'exit', 'roll']

def get_input(*, expected=None, errmsg='', prompt=None):
    """ Automates getting input from user.
        Print prompt, get input, check it is in expected
        if not print errmsg
    """
    if prompt:
        print(prompt)
    if not expected:
        return input('>>> ')
    while True:
        if (user := input('>>> ')) not in expected:
            print(f"{user}: {errmsg}")
            continue
        return user


if __name__ == '__main__':
    s = '1d6'
    print(Azathoth.awaken("roll " + s))
