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
        self.frame_names = []

    def add_df(self, df, sheet_name):
        self.data_frames.append(df)
        self.frame_names.append(sheet_name)

    # pass the list of sheet names and plot those on a graph
    def add_sheets_to_plot(self, sheets=[""]):
        # Check to see if sheets are valid
        for s in sheets:
            for w in self.gm.well_names:
                if s == w:
                    path = f"sheets/csv/{s}.csv"
                    frame = pd.read_csv(path, skiprows=1, usecols=self.columns, parse_dates=[['Date', 'Time']])
                    frame.drop(frame.index[frame['Elevation (ft)'] == '#VALUE!'], inplace=True)
                    frame["Elevation (ft)"] = frame['Elevation (ft)'].astype(float)
                    self.add_df(frame, s)

    
    def plot_sheets(self, chart="line"):
        ax = plt.gca()
        
        for df in self.data_frames:
            df.plot(ax=ax, kind=chart,x='Date_Time',y='Elevation (ft)', marker='.')
            
        ax.legend(self.frame_names)
        ax.set_title('FGCU Hydrogeology Well Elevation (ft)')
        ax.set_xlabel('Date_Time')
        ax.set_ylabel('Elevation (ft)')
        plt.show()
        

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
    
    sheet_name_1 = "sheets/csv/22M.csv" # when doing auto checking, use string len
    sheet_name_2 = "sheets/csv/3A.csv"
    sheet_name_3 = "sheets/csv/MM.csv"
    sheet_name_4 = "sheets/csv/5M.csv"

    """    
    test_frame = pd.read_csv(
        grapher.get_sheet_csv_url(grapher.gm.test_sheet_id, grapher.gm.sheet_ids[grapher.sheet_names[0]]),
        index_col=0)
    """

    test_frame_1 = pd.read_csv(sheet_name_1, skiprows=1, usecols=grapher.columns, parse_dates=[['Date', 'Time']])
    test_frame_2 = pd.read_csv(sheet_name_2, skiprows=1, usecols=grapher.columns, parse_dates=[['Date', 'Time']])
    test_frame_3 = pd.read_csv(sheet_name_3, skiprows=1, usecols=grapher.columns, parse_dates=[['Date', 'Time']])
    test_frame_4 = pd.read_csv(sheet_name_4, skiprows=1, usecols=grapher.columns, parse_dates=[['Date', 'Time']])
    test_frame_3.drop(test_frame_3.index[test_frame_3['Elevation (ft)'] == '#VALUE!'], inplace=True)
    test_frame_4.drop(test_frame_4.index[test_frame_4['Elevation (ft)'] == '#VALUE!'], inplace=True)
    #test_frame_3.drop(test_frame_3.index[test_frame_3['Date_Time'] == '-'], inplace=True)
    test_frame_3["Elevation (ft)"] = test_frame_3['Elevation (ft)'].astype(float)
    test_frame_4["Elevation (ft)"] = test_frame_4['Elevation (ft)'].astype(float)

    grapher.data_frames.append(test_frame_1)
    grapher.data_frames.append(test_frame_2)
    grapher.data_frames.append(test_frame_3)
    grapher.data_frames.append(test_frame_4)


    ax = test_frame_1.plot(kind='line',x='Date_Time',y='Elevation (ft)')
    test_frame_2.plot(kind='line',x='Date_Time',y='Elevation (ft)', ax=ax, marker="h")
    test_frame_3.plot(kind='line',x='Date_Time',y='Elevation (ft)', ax=ax, marker="s")
    test_frame_4.plot(kind='line',x='Date_Time',y='Elevation (ft)', ax=ax, marker="o")
    ax.legend(["22M", "3A", "MM", "5M"])
    ax.ylabel = 'Elevation (ft)'
    plt.show()

    return test_frame_3

def main(stdscr):
    g = SheetsGrapher(GoogleManager())
    g.add_sheets_to_plot(["3A", "5M", "22M", "33M", "MM", "U1"])
    g.plot_sheets()
    #df = test_plot()
    #print(test_frame.head())
    stdscr.clear()
    #stdscr.addstr(0,0,f"{'#VALUE!' in df.values}")
    #stdscr.addstr(2,0,f"{'-' in df.values}")
    stdscr.refresh()
    #stdscr.getch()


#main()
wrapper(main)