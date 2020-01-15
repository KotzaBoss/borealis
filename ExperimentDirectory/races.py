"""
>>> RACE = {'race': {'stats': {'str': 1,  # <-- will be added during char
>>>                            'dex': 1,  #     creation
>>>                            'con': 1,
>>>                            'int': 1,
>>>                            'wis': 1,
>>>                            'cha': 1
>>>                            },
>>>                    'size': 'medium',
>>>                    'speed': 30,
>>>                    'resistance': 'poison'
>>>                    },
"""
RACES = {'human': {'stats': {'str': 1,
                             'dex': 1,
                             'con': 1,
                             'int': 1,
                             'wis': 1,
                             'cha': 1
                             },
                   'size': 'medium',
                   'speed': 30,
                   'resistance': None,
                   'prof': None
                   },
         'dwarf': {'stats': {'str': 0,
                             'dex': 0,
                             'con': 2,
                             'int': 0,
                             'wis': 0,
                             'cha': 0},
                   'size': 'medium',
                   'speed': 25,
                   'damage': {'resist': 'poison',
                              'immune': None,
                              'vulnerable': None,
                              },
                   'prof': {'smith’s tools',
                            'brewer’s supplies',
                            'mason’s tools'}
                   }
         }
