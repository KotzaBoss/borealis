import json
import os
import random as rnd
import sys

import requests

TOP_DIR = os.path.dirname(__file__)
sys.path.append(os.path.dirname(__file__))

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
    class_ = class_.lower()
    race = race.lower()

    class_lvl_init = json.loads(requests.get(f"https://www.dnd5eapi.co/api/classes/{class_}/levels/1").text)
    class_init = json.loads(requests.get(f'https://www.dnd5eapi.co/api/classes/{class_}').text)
    race_init = json.loads(requests.get(f'https://www.dnd5eapi.co/api/races/{race}').text)

    for stat in race_init['ability_bonuses']:
        stat['name'] = stat['name'].lower()
        stats[stat['name']]['score'] += stat['bonus']
        stats[stat['name']]['mod'] = get_mod(stats[stat['name']]['score'])
        stats[stat['name']]['save']['score'] = stats[stat['name']]['mod']

    for stat in class_init['saving_throws']:
        stat['name'] = stat['name'].lower()
        stats[stat['name']]['save']['score'] += class_lvl_init['prof_bonus']
        stats[stat['name']]['save']['prof'] = True

    return stats

# def dice_roller(xdy: str, mem_out=True):
#     """ Generic dice roller. Used in most functions
#
#         :param xdy:
#         :type xdy: str
#         :return: List of rolls or None
#     """
#
#     if xdy is None:
#         err_output('no args for regex')
#         return
#
#     roll_pattern = r"(\d+)d(\d+)"
#     match = re.search(roll_pattern, xdy, re.IGNORECASE)
#
#     if not match:
#         err_output('No match. Expected xdy')
#         return
#
#     if match.group(1)[0] == '0' or match.group(2)[0] == '0':
#         err_output('Bad arguments, Try again')
#         return
#
#     if match:
#         rolls = []
#         for i in range(int(match.group(1))):
#             rolls.append(rnd.randint(1, int(match.group(2))))
#         if mem_out:
#             mem_output(f"{rolls}")
#         return rolls
#
#
# def death_save_roll(dist: int = None):
#     if dist:
#         if dist <= 5:
#             return {'success': 0,
#                     'failures': 2}
#         else:
#             return {'success': 0,
#                     'failures': 1}
#
#     roll = dice_roller('1d20', mem_out=False)[0]
#     if roll == 20:
#         return None
#     elif roll > 10:
#         return {'success': 1,
#                 'failures': 0}
#     elif roll > 1:
#         return {'success': 0,
#                 'failures': 1}
#     else:
#         return {'success': 0,
#                 'failures': 2}
