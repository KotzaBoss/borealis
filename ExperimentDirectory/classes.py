import random as rnd

from .armors import LIGHT_ARMORS, NO_ARMOR
from .weapons import WEAPONS

rnd.seed(666)

CLASSES = {'ranger': {'init_hp': 10 + rnd.randint(1, 10),
                      'hit_dice': '1d10',
                      'lvlup_mod': 'con',
                      'hp_incr': '1d10',
                      'saves': ('str', 'dex'),
                      'skill_prof': {'skills': {'animal handling',
                                                'athletics',
                                                'insight',
                                                'investigation',
                                                'nature',
                                                'perception',
                                                'stealth',
                                                'survival'},
                                     'num': 2
                                     },
                      'armor': LIGHT_ARMORS['leather'],
                      'lvls': {1: {'prof': 2,
                                   'features': {
                                       'favored enemy': {'descr': 'choose enemy, learn their language if they have one',
                                                         'fx': 'adv to wis, int checks on favored enemy'},
                                       'natural explorer': {
                                           'descr': 'choose terain int, wis checks on it are calced with 2*prof',
                                           'fx': "Difficult terrain doesn’t slow your group’s travel.\n"
                                                 "Your group can’t become lost except by magical means.\n"
                                                 "Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.\n"
                                                 "If you are traveling alone, you can move stealthily at a normal pace.\n"
                                                 "When you forage, you find twice as much food as you normally would.\n"
                                                 "While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area."}
                                   }
                                   }
                               }
                      },
           'barbarian': {'init_hp': 12 + rnd.randint(1, 12),
                         'hit_dice': '1d12',
                         'lvlup_mod': 'con',
                         'hp_incr': '1d12',
                         'saves': ('str', 'con'),
                         'skill_prof': {'skills': {'animal handling',
                                                   'athletics',
                                                   'intimidation',
                                                   'nature',
                                                   'perception',
                                                   'survival'},
                                        'armor': ('light armor',
                                                  'medium armor',
                                                  'shields'),
                                        'weapons': ('simple weapons',
                                                    'martial weapons'),
                                        'num': 2
                                        },
                         'armor': NO_ARMOR,
                         'weapons': (WEAPONS['greataxe'], WEAPONS['shortsword']),
                         'lvls': {1: {'prof': 2,
                                      'features': {'rage': {
                                          'descr': 'You have advantage on Strength checks and Strength saving throws.\n'
                                                   'When you make a melee _weapon attack_roll using Strength, you gain a bonus to the damage_roll roll that increases as you gain levels as a barbarian, as shown in the Rage Damage column of the Barbarian table.'
                                                   'You have resistance to bludgeoning, piercing, and slashing damage_roll.'},
                                          'unarmored defense': {
                                              'descr': 'While you are not wearing any armor, your Armor Class equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit.',
                                          }
                                      }
                                      }
                                  }
                         }

           }
