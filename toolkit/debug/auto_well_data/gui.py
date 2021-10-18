"""
 Handle the GUI and interactions
 with the user.
 Will be the maine executable
"""
import tkinter as tk
from tkinter import *

import html_reader as hr

import sheets_manager as sm

# TODO Setup window size
# Add buttons and shit
# Figure out how to select files from HD
# connect to Google Sheet API

# Setup our window
root = Tk()

html_reader = hr.HtmlReader
sheets_manager = sm.SheetsManager

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
TITLE = "Hydrogeology Well Data Processor v0.1"

# TODO setup connection to google sheets
connected_to_sheets = False 

# Setup the buttons
# TODO need to setup locations for everything
select_html_file_button = Button(root, text="b1", command=None)
select_manual_well_data_button = Button(root, text="b2")
generate_sheet_button = Button(root, text="b2")

def main():
    pass

if __name__ == "__main__":
    main()
