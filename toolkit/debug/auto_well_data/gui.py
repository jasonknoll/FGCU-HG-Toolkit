"""
 Handle the GUI and interactions
 with the user.
 Will be the maine executable
"""
import tkinter as tk
from tkinter import *

import html_reader as hr

import sheets_manager as sm

# import openpyxl

# TODO Setup window size
# Add buttons and shit
# Figure out how to select files from HD
# connect to Google Sheet API

# Setup our window
root = Tk()

html_reader = hr.HtmlReader()
sheets_manager = sm.SheetsManager()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
TITLE = "Hydrogeology Well Data Processor v0.1"

# TODO setup connection to google sheets
connected_to_sheets = False 

# Setup the buttons
# TODO need to setup locations for everything
select_html_file_button = Button(root, text="Upload HTML File", command=None, padx=20, pady=20)
select_html_file_button.grid(row=0, column=0)

select_manual_well_data_button = Button(root, text="Upload Manual Well Measurement", padx=20, pady=20)
select_manual_well_data_button.grid(row=0, column=1)

generate_sheet_button = Button(root, text="Generate New Sheet", padx=20, pady=20)
generate_sheet_button.grid(row=0, column=2)

# Handle all things necessary to connect to google account
def connect_to_sheets():
    pass

def main():
    root.mainloop()

if __name__ == "__main__":
    main()
