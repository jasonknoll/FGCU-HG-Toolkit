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

# plot shit before I get everything organized
"""
 Using this test plot info:
    + learn to iterate through the list of frames
    + remove the null values from every plot
    + Stop using pandas' plot shortcut 
    + Read file names automatically to

 When I'm feeling really out there
    + Allow user to select the wells needed to be graphed
    + Let user pick colors

"""
def test_plot(well=""):
    grapher = SheetsGrapher(GoogleManager())
    
    sheet_name_1 = "sheets/csv/WellMeasurementsNewFormatUpdatedTest - 22M.csv" # when doing auto checking, use string len
    sheet_name_2 = "sheets/csv/WellMeasurementsNewFormatUpdatedTest - 3A.csv"
    sheet_name_3 = "sheets/csv/WellMeasurementsNewFormatUpdatedTest - MM.csv"

    """    
    test_frame = pd.read_csv(
        grapher.get_sheet_csv_url(grapher.gm.test_sheet_id, grapher.gm.sheet_ids[grapher.sheet_names[0]]),
        index_col=0)
    """

    test_frame_1 = pd.read_csv(sheet_name_1, skiprows=1, usecols=grapher.columns, parse_dates=[['Date', 'Time']])
    test_frame_2 = pd.read_csv(sheet_name_2, skiprows=1, usecols=grapher.columns, parse_dates=[['Date', 'Time']])
    test_frame_3 = pd.read_csv(sheet_name_3, skiprows=1, usecols=grapher.columns, parse_dates=[['Date', 'Time']])
    test_frame_3.drop(test_frame_3.index[test_frame_3['Elevation (ft)'] == '#VALUE!'], inplace=True)
    #test_frame_3.drop(test_frame_3.index[test_frame_3['Date_Time'] == '-'], inplace=True)
    test_frame_3["Elevation (ft)"] = test_frame_3['Elevation (ft)'].astype(float)

    grapher.data_frames.append(test_frame_1)
    grapher.data_frames.append(test_frame_2)
    grapher.data_frames.append(test_frame_3)


    ax = test_frame_1.plot(kind='line',x='Date_Time',y='Elevation (ft)')
    test_frame_2.plot(kind='line',x='Date_Time',y='Elevation (ft)', ax=ax)
    test_frame_3.plot(kind='line',x='Date_Time',y='Elevation (ft)', ax=ax)
    ax.legend(["22M", "3A", "MM"])
    ax.ylabel = 'Elevation (ft)'
    plt.show()

    return test_frame_3

def main(stdscr):
    df = test_plot()
    #print(test_frame.head())
    stdscr.clear()
    #stdscr.addstr(0,0,f"{'#VALUE!' in df.values}")
    #stdscr.addstr(2,0,f"{'-' in df.values}")
    stdscr.refresh()
    #stdscr.getch()


#main()
wrapper(main)