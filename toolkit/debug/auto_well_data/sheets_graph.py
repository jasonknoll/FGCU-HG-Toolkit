from gui import GUI
from sheets_manager import GoogleManager
import curses
from curses import wrapper

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class SheetsGrapher():
    def __init__(self, gm=GoogleManager()):
        self.gm = gm
        if (not gm):
            gm = GoogleManager()

        self.sheet_names = gm.well_names
        self.sheet_ids = gm.sheet_ids
        
        # turn all sheets into dataframes
        # for now start with just 22M


def main(stdscr):
    grapher = SheetsGrapher(GoogleManager())
    stdscr.clear()
    stdscr.addstr(0,0,"it works at least press enter to continue...")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)