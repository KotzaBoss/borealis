import sys
sys.path.append('/home/kotzaboss/Git')  # TODO:
from utils.roll import standard_table

CMDS = ['new', 'import', 'exit']
INIT_ROLLS = {'std': standard_table,
              'pointbuy': None,
              '3d6': None,
              '4d6max3': None,
              '4d6reroll1': None,
              'custom': None}

def get_input(*, expected=None, errmsg='', prompt='>>> '):
    if not expected:
        return input(prompt)
    while True:
        if (user := input(prompt)) not in expected:
            print(f"{user}: {errmsg}")
            continue
        return user


while True:
    print(CMDS)
    user = get_input(expected=CMDS, errmsg='Unavailable command')
    if user == 'exit':
        break
    if user == 'new':
        user = get_input(expected=INIT_ROLLS.keys(), errmsg='Unavailable roll type')
