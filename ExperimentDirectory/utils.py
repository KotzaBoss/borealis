import curses
import random as rnd
import re

from colorama import init

from .classes import CLASSES
from .cursed_functions import mem_output, cmdline_input, err_output
from .cursed_windows import WinPos
from .races import RACES

# Uncomment for debug (keep random sequence the same)
rnd.seed(666)

STATS = {'str': {'score': 0, 'mod': 0, 'save': {'score': 0, 'prof': False}},
         'dex': {'score': 0, 'mod': 0, 'save': {'score': 0, 'prof': False}},
         'con': {'score': 0, 'mod': 0, 'save': {'score': 0, 'prof': False}},
         'int': {'score': 0, 'mod': 0, 'save': {'score': 0, 'prof': False}},
         'wis': {'score': 0, 'mod': 0, 'save': {'score': 0, 'prof': False}},
         'cha': {'score': 0, 'mod': 0, 'save': {'score': 0, 'prof': False}}
         }

score_mod = {range(0, 2): -5,
             range(2, 4): -4,
             range(4, 6): -3,
             range(6, 8): -2,
             range(8, 10): -1,
             range(10, 12): 0,
             range(12, 14): 1,
             range(14, 16): 2,
             range(16, 18): 3,
             range(18, 20): 4,
             range(20, 22): 5,
             range(22, 24): 6,
             range(24, 26): 7,
             range(26, 28): 8,
             range(28, 30): 9,
             range(30, 32): 10
             }


def get_mod(score):
    for range_ in score_mod:
        if score in range_:
            return score_mod[range_]


init(autoreset=True)


def init_stat_roll(race: str, class_: str):
    """ Rolls two columns of stats. Ensure the calcs are accoding to the rules """
    columns = []
    for attempt in range(1, 3):  # 2 COLUMNS
        roll_sum = [0, 0, 0, 0, 0, 0]
        for i in range(6):  # 6 STATS
            tmp_rolls = []
            for j in range(4):  # 4d6
                roll = rnd.randint(1, 6)
                if roll == 1:  # Uncertain about rules. Is it rerolled once?????
                    roll = rnd.randint(1, 6)
                tmp_rolls.append(roll)
            tmp_rolls.sort()
            for k in range(1, len(tmp_rolls)):
                roll_sum[i] = roll_sum[i] + tmp_rolls[k]
        columns.append(roll_sum)

    c1 = columns[0]
    c2 = columns[1]

    ret = f"{15 * ' '}C1 | C2\n" \
          f"{(15 + len('C1 | C2')) * '-'}\n"
    for n1, n2 in zip(c1, c2):
        ret += f"{15 * ' '}{n1:>2d} | {n2:>2d}\n"

    mem_output(ret, prompt=False)

    # Get user input. Which column they'll use
    cx = {'1': (WinPos.COL1_POS, c1), '2': (WinPos.COL2_POS, c2)}
    while True:
        choice = cmdline_input('Choose col')
        if choice in cx.keys():
            kept_col = (choice, cx.pop(choice))
            for i in range(len(STATS.keys())):
                WinPos.windows['memory_win'].addstr(WinPos.STAT_POS + i, next(iter(cx.values()))[0], '  ')
                WinPos.windows['memory_win'].refresh()
            WinPos.set_state('ok')
            break
        else:
            WinPos.set_state('error')

    WinPos.windows['win'].refresh()

    # Show _stat column
    for d, i, j, stat in zip(range(len(STATS)), c1, c2, STATS):
        WinPos.windows['memory_win'].addstr(WinPos.STAT_POS + d, 0, stat + ':')
        WinPos.windows['memory_win'].refresh()

    # Get user input. Check if input is in kept_col and keep index for later inputs.
    found_indexes = []
    for i, stat in enumerate(STATS):
        while True:
            try:
                inp = int(WinPos.windows['memory_win'].getstr(WinPos.STAT_POS + i, WinPos.STAT_CURSOR_POS, 2))
                # inp = int(cmdline_input(f"Allocate {_stat} score"))
            except ValueError:
                WinPos.windows['memory_win'].addstr(WinPos.STAT_POS + i, WinPos.STAT_CURSOR_POS, '  ')
                WinPos.windows['memory_win'].refresh()
                continue
            else:
                for index, val in enumerate(kept_col[1][1]):
                    if inp == val:
                        if index in found_indexes:
                            continue
                        found_indexes.append(index)
                        STATS[stat]['score'] = inp
                        WinPos.windows['memory_win'].addstr(WinPos.STAT_POS + index, kept_col[1][0], f"{inp:>2d}",
                                                            curses.A_UNDERLINE)
                        WinPos.windows['memory_win'].refresh()
                        break
                else:
                    WinPos.set_state('error')
                    err_output('Error')
                    WinPos.windows['memory_win'].addstr(WinPos.STAT_POS + i, WinPos.STAT_CURSOR_POS, '  ')
                    WinPos.windows['memory_win'].refresh()
                    continue

            finally:
                WinPos.add_counter()

            break
    else:
        WinPos.set_state('ok')
        for stat in STATS:
            STATS[stat]['score'] += RACES[race]['stats'][stat]
            STATS[stat]['mod'] = get_mod(STATS[stat]['score'])
            STATS[stat]['save']['score'] = STATS[stat]['mod']
            if stat in CLASSES[class_]['saves']:
                STATS[stat]['save']['score'] += CLASSES[class_]['lvls'][1]['prof']
                STATS[stat]['save']['prof'] = True
        return STATS


def dice_roller(xdy: str, mem_out=True):
    """ Generic dice roller. Used in most functions

        :param xdy:
        :type xdy: str
        :return: List of rolls or None
    """

    if xdy is None:
        err_output('no args for regex')
        return

    roll_pattern = r"(\d+)d(\d+)"
    match = re.search(roll_pattern, xdy, re.IGNORECASE)

    if not match:
        err_output('No match. Expected xdy')
        return

    if match.group(1)[0] == '0' or match.group(2)[0] == '0':
        err_output('Bad arguments, Try again')
        return

    if match:
        rolls = []
        for i in range(int(match.group(1))):
            rolls.append(rnd.randint(1, int(match.group(2))))
        if mem_out:
            mem_output(f"{rolls}")
        return rolls


def death_save_roll(dist: int = None):
    if dist:
        if dist <= 5:
            return {'success': 0,
                    'failures': 2}
        else:
            return {'success': 0,
                    'failures': 1}

    roll = dice_roller('1d20', mem_out=False)[0]
    if roll == 20:
        return None
    elif roll > 10:
        return {'success': 1,
                'failures': 0}
    elif roll > 1:
        return {'success': 0,
                'failures': 1}
    else:
        return {'success': 0,
                'failures': 2}
