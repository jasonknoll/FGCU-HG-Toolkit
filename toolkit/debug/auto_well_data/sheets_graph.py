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
        self.columns = ["Date", "Time", "Elevation (ft)"]

        self.data_frames = []

    def get_sheet_csv_url(self, key, sid):
        return f"https://docs.google.com/spreadsheets/d/{key}/export?gid={sid}&format=csv"

    def load_csv_from_file(self, path):
        pass


def main(stdscr):
    grapher = SheetsGrapher(GoogleManager())
    
    sheet_name = "sheets/WellMeasurementsNewFormatUpdatedTest - 22M.csv"
    """    test_frame = pd.read_csv(
        grapher.get_sheet_csv_url(grapher.gm.test_sheet_id, grapher.gm.sheet_ids[grapher.sheet_names[0]]),
        index_col=0)
    """
    test_frame = pd.read_csv(sheet_name, skiprows=1, usecols=grapher.columns, parse_dates=[['Date', 'Time']])
    grapher.data_frames.append(test_frame)
    #print(test_frame.head())
    stdscr.clear()
    stdscr.addstr(0,0,test_frame.to_string())
    stdscr.refresh()
    stdscr.getch()


#main()
wrapper(main)