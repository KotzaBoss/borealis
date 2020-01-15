import curses
from time import sleep

from .cursed_windows import WinPos


def reset_cmdline():
    WinPos.windows['cmdline'].addstr(0, 0, WinPos.state['prompt'])
    WinPos.windows['cmdline'].refresh()

WinPos.last_cmd = ''


def cmdline_input(msg='', prompt=True) -> str:
    """ Standardised input waiting command line string

        **CAUTION RETURNS STR!**
    """
    WinPos.windows['cmdline'].addstr(0, 0, '                            ')

    if prompt:
        WinPos.windows['cmdline'].addstr(0, 0, f"{WinPos.state['prompt']}{str(msg)}")
        WinPos.windows['cmdline'].refresh()
        WinPos.last_cmd = str(WinPos.windows['cmdline'].getstr(0, len(WinPos.state['prompt'] + str(msg)) + 1, 30))[2:-1]
        return WinPos.last_cmd
    else:
        WinPos.windows['cmdline'].addstr(0, 0, str(msg))
        WinPos.windows['cmdline'].refresh()
        WinPos.last_cmd = str(WinPos.windows['cmdline'].getstr(0, len(msg), 30))[2:-1]
        return WinPos.last_cmd


def mem_output(msg='', prompt=False):
    """ Print standardised output to memory window (over cmdline)"""
    if prompt:

        WinPos.windows['memory_win'].addstr(WinPos.MEM_HEIGHT - 1, 1,
                                            f"{WinPos.state['prompt']}{WinPos.last_cmd}\n{str(msg)}")
    else:
        WinPos.windows['memory_win'].addstr(WinPos.MEM_HEIGHT - 1, 1,
                                            str(msg))
    WinPos.windows['memory_win'].scroll(1)
    # WinPos.windows['memory_win'].insdelln(-1)
    WinPos.windows['memory_win'].border(0,0,0,0,0,0,0,0)
    WinPos.windows['memory_win'].refresh()
    # reset_cmdline()


def err_output(msg=''):
    """ Print a standardised error message to error window (below cmdline) """
    WinPos.windows['err_win'].insertln()
    WinPos.windows['err_win'].insstr(1, 1, f"{WinPos.state['prompt']}{WinPos.last_cmd}\n{str(msg)}")
    WinPos.windows['err_win'].border(0,0,0,0,0,0,0,0)
    WinPos.windows['err_win'].refresh()
    # reset_cmdline()


def exit_(msg=''):
    WinPos.windows['win'].clear()
    WinPos.windows['win'].addstr(10, 10, f"{str(msg)}", curses.A_BOLD)
    WinPos.windows['win'].refresh()
    sleep(2)
    curses.endwin()
