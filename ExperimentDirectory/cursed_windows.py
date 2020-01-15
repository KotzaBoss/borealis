# import curses

class WinPos:
    windows = {'win': None,
               'memory_win': None,
               'err_win': None,
               'cmdline': None,
               'ln_counter': 1}

    CMD_HEIGHT = 1
    CMD_START_POS = 29
    CMD_PROMPT_POS = 0
    CMD_PROMPT_ERR_POS = CMD_PROMPT_POS + 2

    MEM_HEIGHT = 23
    MEM_START_POS = CMD_START_POS - MEM_HEIGHT

    ERR_HEIGHT = 10
    ERR_START_POS = CMD_START_POS + 1

    COL1_POS = 15
    COL_SEP_POS = 8
    COL2_POS = 20
    STAT_POS = MEM_START_POS + MEM_HEIGHT - 14
    STAT_CURSOR_POS = 5

    CMD_OK_PROMPT = ''
    CMD_ERR_PROMPT = ''

    ERR_WIN_PROMPT = ''

    STATES = {'ok': {'prompt': CMD_OK_PROMPT,
                     'cursor': len(CMD_OK_PROMPT) + 1
                     },
              'error': {'prompt': CMD_ERR_PROMPT,
                        'cursor': len(CMD_ERR_PROMPT) + 1
                        }
              }

    last_cmd = ''

    state = {}

    @classmethod
    def init(cls):
        """ Initialise """
        cls.CMD_OK_PROMPT = f"[1] >> "
        cls.CMD_ERR_PROMPT = f"X [1] >> "

        cls.ERR_WIN_PROMPT = f"[1] "

        cls.STATES = {'ok': {'prompt': cls.CMD_OK_PROMPT,
                             'cursor': len(cls.CMD_OK_PROMPT) + 1,
                             'state': 'ok'
                             },
                      'error': {'prompt': cls.CMD_ERR_PROMPT,
                                'cursor': len(cls.CMD_ERR_PROMPT) + 1,
                                'state': 'error'
                                },
                      }

        cls.state = {'prompt': cls.CMD_OK_PROMPT,
                     'cursor': len(cls.CMD_OK_PROMPT) + 1,
                     'state': 'ok'}

    @classmethod
    def add_counter(cls):
        cls.windows['ln_counter'] += 1
        cls.CMD_OK_PROMPT = f"[{cls.windows['ln_counter']}] >> "
        cls.CMD_ERR_PROMPT = f"X [{cls.windows['ln_counter']}] >> "

        cls.CMD_CURSOR_POS = len(cls.CMD_OK_PROMPT) + 1
        cls.CMD_CURSOR_ERR_POS = len(cls.CMD_ERR_PROMPT) + 1

        cls.ERR_WIN_PROMPT = f"[{cls.windows['ln_counter']}] "

        cls.STATES.update({'ok': {'prompt': cls.CMD_OK_PROMPT,
                                  'cursor': len(cls.CMD_OK_PROMPT) + 1,
                                  'state': 'ok'
                                  },
                           'error': {'prompt': cls.CMD_ERR_PROMPT,
                                     'cursor': len(cls.CMD_ERR_PROMPT) + 1,
                                     'state': 'error'
                                     }
                           }
                          )
        cls.state.update(cls.STATES[cls.state['state']])

    @classmethod
    def set_state(cls, st):
        if st == 'error':
            cls.state.update(cls.STATES['error'])
        else:
            cls.state.update(cls.STATES['ok'])
