"""
TODO:
    - [ ] Deal with resizing (doesnt seem easy)
"""
import curses
import inspect

from . import __version__
from .characters import create_character, show_character, delete_character, read_character, CHARACTERS
from .cursed_functions import err_output, cmdline_input, mem_output, exit_
from .cursed_windows import WinPos
from .utils import init_stat_roll, dice_roller


def help_(command: str = None) -> None:
    if command:
        mem_output(f"{inspect.getsourcelines(COMMANDS[command]['func'])[0][0]}\n{COMMANDS[command]['help']}")
    else:
        mem_output(f"help {inspect.getsourcelines(COMMANDS['help']['func'])[0][0]}\n{COMMANDS['help']['help']}")


COMMANDS = {'new': {'func': create_character, 'help': 'New character'},
            'read': {'func': read_character, 'help': 'Read from character'},
            'delete': {'func': delete_character, 'help': 'Delete character'},
            'show': {'func': show_character, 'help': 'Display a character'},
            'roll': {'func': dice_roller, 'help': 'Roll dy die, x times'},
            'init': {'func': init_stat_roll, 'help': 'Roll two columns of character creaton stats'},
            'exit': {'func': 'Shell.rmv_credit', 'help': 'Self explanatory'},
            'help': {'func': help_, 'help': "Type 'help <command>' to get more information"}
            }


def curses_init():
    """ Main loop

        user input -> function/error -> output -> repeat
    """
    # Initialise main window and colors
    WinPos.windows['win'] = curses.initscr()

    curses.update_lines_cols()
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_MAGENTA, -1)
    curses.cbreak()
    # curses.noecho()

    # Initialise command line and memory window, error window
    WinPos.windows['cmdline'] = curses.newwin(WinPos.CMD_HEIGHT, curses.COLS - 2, WinPos.CMD_START_POS, 1)
    WinPos.windows['memory_win'] = curses.newwin(WinPos.MEM_HEIGHT, curses.COLS - 2, WinPos.MEM_START_POS,                                                     1)
    WinPos.windows['err_win'] = curses.newwin(WinPos.ERR_HEIGHT, curses.COLS - 2, WinPos.ERR_START_POS, 1)
    WinPos.windows['cmdline'].keypad(True)
    WinPos.windows['memory_win'].keypad(True)
    WinPos.windows['err_win'].keypad(True)
    WinPos.init()


    # Not sure it works
    WinPos.windows['cmdline'].scrollok(True)
    WinPos.windows['err_win'].scrollok(True)
    WinPos.windows['memory_win'].scrollok(True)
    # WinPos.windows['memory_win'].setscrreg(0, WinPos.MEM_HEIGHT - 1)
    resizeHandler()
    # Greeting text
    greeting_txt()

    WinPos.windows['memory_win'].refresh()
    WinPos.windows['err_win'].refresh()


def resizeHandler(signum=None, frame=None):
    WinPos.windows['win'].erase()
    WinPos.windows['memory_win'].erase()
    WinPos.windows['err_win'].erase()

    greeting_txt()

    # try:
    #     mem_output(f"resize-window signal caught - {curses.COLS}")
    # except Exception as e:
    #     pass
    # corner_symbol = '*'
    WinPos.windows['win'].border(0, 0, 0, 0, 0, 0, 0, 0)
    #
    # WinPos.windows['win'].addstr(WinPos.MEM_START_POS, 0, corner_symbol)  # upper left
    # WinPos.windows['win'].addstr(WinPos.MEM_START_POS + WinPos.MEM_HEIGHT - 1, 0, corner_symbol)  # lower left
    # WinPos.windows['win'].addstr(WinPos.MEM_START_POS, curses.COLS - 1, corner_symbol)  # upper right
    # WinPos.windows['win'].addstr(WinPos.MEM_START_POS + WinPos.MEM_HEIGHT - 1, curses.COLS - 1, corner_symbol)  # upper right
    #
    # WinPos.windows['win'].addstr(WinPos.ERR_START_POS, 0, corner_symbol)
    # WinPos.windows['win'].addstr(WinPos.ERR_START_POS + WinPos.ERR_HEIGHT - 1, 0, corner_symbol)
    # WinPos.windows['win'].addstr(WinPos.ERR_START_POS, curses.COLS - 1, corner_symbol)
    # WinPos.windows['win'].addstr(WinPos.ERR_START_POS + WinPos.ERR_HEIGHT - 1, curses.COLS - 1, corner_symbol)
    WinPos.windows['memory_win'].border(0, 0, 0, 0, 0, 0, 0, 0)
    WinPos.windows['err_win'].border(0, 0, 0, 0, 0, 0, 0, 0)

    WinPos.windows['win'].refresh()
    WinPos.windows['memory_win'].refresh()
    WinPos.windows['err_win'].refresh()


def loop():
    read_character()
    rows, cols = WinPos.windows['win'].getmaxyx()
    while True:
        try:
            user_in = cmdline_input()
            nrows, ncols = WinPos.windows['win'].getmaxyx()
            if nrows != rows or ncols != cols:
                rows, cols = nrows, ncols
                mem_output(f"{rows} {cols}")
                # curses.resize_term(rows, cols)
                WinPos.windows['win'].resize(rows, cols)
                WinPos.windows['cmdline'].resize(rows, cols-2)
                WinPos.windows['memory_win'].resize(rows, cols-2)
                WinPos.windows['err_win'].resize(rows, cols-2)
                resizeHandler()

            if user_in == 'exit':
                exit_('Goodbye!')
                return

            elif ' ' in user_in:
                cmd, *args = user_in.split(' ')
                if cmd in CHARACTERS:
                    if args[0] in {'receive', 'combat'}:
                        getattr(CHARACTERS[cmd], f"{args[0]}")(*args[1:])
                    else:
                        raise AttributeError
                else:
                    COMMANDS[cmd]['func'](*args)

            else:
                COMMANDS[user_in]['func']()

        except Exception as e:
            WinPos.set_state('error')
            err_output(f"{e}")

        else:
            WinPos.set_state('ok')
            # mem_output(f"{user_in}\n")

        finally:
            WinPos.add_counter()


def greeting_txt():
    WinPos.windows['win'].addstr(1, 5, 'B O R E A L I S', curses.color_pair(1) + curses.A_BOLD)
    WinPos.windows['win'].addstr(1, (curses.COLS - 1) - len(__version__), __version__, curses.A_DIM)
    WinPos.windows['win'].addstr(3, 1, f"Commands: {[cmd for cmd in COMMANDS.keys() if cmd not in {'help', '>>--->'}]}")
    WinPos.windows['win'].addstr(4, 1, f"Type help <command> for more information")
    WinPos.windows['win'].refresh()
