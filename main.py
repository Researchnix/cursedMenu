import numpy as np
import curses
from curses import textpad
import time

# ideas

# make this into a class
# It can take a nested dictionary to display
# a menu in Apple finder column view style

# one parameter determines whether the column width is constant,
# maximal or flexible

# The position in the tree network of the menu can be stored as a list
# with number of selection on each level of the menu

# one method should be to obtain the value of the current selection 


def initializeColumn(stdscr, menu):
    width = max(map(lambda x: len(x), menu))
    ymax, xmax = stdscr.getmaxyx()
    for i in range(ymax):
        stdscr.addstr(i, width, '|')
    stdscr.refresh()


def updateDisplay(stdscr, menu, selection):
    if selection < 0:
        selection = 0
    elif selection > len(menu) - 1:
        selection = len(menu) - 1

    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)


    ymax, xmax = stdscr.getmaxyx()

    line = 0
    for m in menu:
        if line == selection:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(line, 0, m)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(line, 0, m)
        line += 1
    stdscr.refresh()
    return selection


def main(stdscr):

    menu = ['portfolio', 'watchlist', 'add']
    initializeColumn(stdscr, menu)
    selection = updateDisplay(stdscr, menu, 0)
    while True:
        ans = stdscr.getch()

        if ans == ord('q'):
            break
        elif ans == ord('j'):
            selection = updateDisplay(stdscr, menu, selection + 1)
        elif ans == ord('k'):
            selection = updateDisplay(stdscr, menu, selection - 1)



curses.wrapper(main)

