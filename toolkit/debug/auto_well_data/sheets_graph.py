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
        self.data_frames = []

    def get_sheet_csv_url(self, wbid, sid):
        return f"https://docs.google.com/spreadsheets/d/{wbid}/export?gid={sid}&format=csv"


def main(stdscr):
    grapher = SheetsGrapher(GoogleManager())
    
    test_frame = pd.read_csv(
        grapher.get_sheet_csv_url(grapher.gm.test_sheet_id, grapher.gm.sheet_ids[grapher.sheet_names[0]]),
        error_bad_lines=False)
    grapher.data_frames.append(test_frame)
    test_frame = test_frame.astype('string')
    stdscr.clear()
    stdscr.addstr(0,0,test_frame.head())
    stdscr.refresh()
    stdscr.getch()

wrapper(main)