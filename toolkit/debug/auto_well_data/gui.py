"""
 Handle the GUI and interactions
 with the user.
 Will be the maine executable
"""

import os


import tkinter.filedialog
import tkinter as tk
from tkinter import *

import html_reader as hr

import sheets_manager as sm

# import openpyxl

# TODO Setup window size
# Add buttons and shit
# Figure out how to select files from HD
# connect to Google Sheet API
# Setup OpenpyXL

# Setup our window
# TODO organize buttons and labels into frames
root = Tk()
root.geometry("640x480")

button_frame = LabelFrame(root, text="Auto Well Data Processor", width=480, height=140, bd=5)
button_frame.pack()
button_frame.pack_propagate(False)

label_frame = LabelFrame(root, width=480, height=200)
label_frame.pack()


html_reader = hr.HtmlReader()
sheets_manager = sm.SheetsManager()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
TITLE = "Hydrogeology Well Data Processor v0.1"

# TODO setup connection to google sheets
connected_to_sheets = False 


html_file_path_label = Label(label_frame, text=f'Selected HTML file: none', justify="center", wraplength=550)
html_file_path_label.pack()

# Setup the buttons
# TODO need to setup locations for everything

def update_html_file_path(label, hr):
    hr.set_curr_file_path(tkinter.filedialog.askopenfilename())
    if (hr.get_curr_file_path()):
        label.config(text = f'Seelcted HTML file: {hr.get_curr_file_path()}')
        label.pack()
    
    
select_html_file_button = Button(button_frame, text="Upload HTML File", command= lambda: update_html_file_path(html_file_path_label, html_reader), pady=7)
select_html_file_button.pack()


select_manual_well_data_button = Button(button_frame, text="Upload Manual Well Measurement Sheet", pady=7)
select_manual_well_data_button.pack()


generate_sheet_button = Button(button_frame, text="Generate New Sheet", pady=5)
generate_sheet_button.pack()


# Handle all things necessary to connect to google account
def connect_to_sheets():
    pass

def main():
    #root.resizable(False, False)
    #root.grid_propagate(False)
    root.mainloop()

if __name__ == "__main__":
    main()
