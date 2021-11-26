from gui import GUI
from sheets_manager import GoogleManager
import curses
from curses import wrapper

import numpy as np

class SheetsGrapher():
    def __init__(self, gm=GoogleManager()):
        self.gm = gm
        if (not gm):
            gm = GoogleManager()

def main(stdscr):
    grapher = SheetsGrapher(GoogleManager())
    stdscr.clear()
    stdscr.addstr(0,0,"it works at least press enter to continue...")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)