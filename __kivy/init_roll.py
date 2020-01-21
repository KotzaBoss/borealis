import random as rnd

from pyqt.classes import CLASSES
from pyqt.races import RACES
from pyqt.utils import get_mod


def init_stat_roll():
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

    return c1, c2


def finalise_init(race, class_, stats):
    for stat in stats:
        stats[stat]['score'] += RACES[race]['stats'][stat]
        stats[stat]['mod'] = get_mod(stats[stat]['score'])
        stats[stat]['save']['score'] = stats[stat]['mod']
        if stat in CLASSES[class_]['saves']:
            stats[stat]['save']['score'] += CLASSES[class_]['lvls'][1]['prof']
            stats[stat]['save']['prof'] = True
    return stats
