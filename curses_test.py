#!/usr/bin/env python3

"""
Curses module test
"""

import curses

stdscr = curses.initscr()
print("stdscr: %s" % stdscr)
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0, 10, "Hit q to quit")
stdscr.refresh()

key = ''

if __name__ == "__main__":

    pass
