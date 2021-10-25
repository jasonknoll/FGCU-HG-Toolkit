"""
 Handle the GUI and interactions
 with the user.
 Will be the maine executable
"""

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
# TODO Look at email from Lane

# Setup our window
# TODO organize buttons and labels into frames
"""
root = Tk()
root.geometry("640x480")
root.title("HG-Well-Data-Toolkit v0.1")
root.iconbitmap('logoicon.ico')

button_frame = LabelFrame(root, text="Auto Well Data Processor", width=480, height=140, bd=5)
button_frame.pack()
button_frame.pack_propagate(False)

label_frame = LabelFrame(root, width=480, height=200)
label_frame.pack()


html_reader = hr.HtmlReader()
sheets_manager = sm.SheetsManager()

# TODO setup connection to google sheets
connected_to_sheets = False 


html_file_path_label = Label(label_frame, text=f'Selected HTML file: none', justify="center", wraplength=550)
html_file_path_label.pack()

# TODO Pickup from here 10/22/2021
manual_data_path_label = Label(label_frame, text='Selected well-data file: none', justify="center", wraplength=550, pady=10)
manual_data_path_label.pack()

# Setup the buttons
# TODO need to setup locations for everything

def get_file_type(path):
    rev = path[::-1]
    f_type = ""
    for r in rev:
        if (not r == '.'):
            f_type += r
        else:
            break
    return f_type[::-1]

# TODO figure out file path labels
def update_html_file_path(label, hr):
    hr.set_curr_file_path(tkinter.filedialog.askopenfilename(filetypes=[("htm files", ".htm"),("html files", ".html")]))                       
    if (hr.get_curr_file_path()):
        label.config(text = f'Selected {get_file_type(hr.get_curr_file_path())} file: {hr.get_curr_file_path()}')
        label.pack()
        
    
select_html_file_button = Button(button_frame, text="Upload HTML File", command= lambda: update_html_file_path(html_file_path_label, html_reader), pady=7)
select_html_file_button.pack()


def update_manual_data_path(label, sm):
    sm.set_manual_data_path(tkinter.filedialog.askopenfilename(filetypes=[("excel files", ".xlsx")]))
    if (sm.get_manual_data_path):
        label.config(text=f'Selected manual data sheet file: {sm.get_manual_data_path()}')
        label.pack()


select_manual_well_data_button = Button(button_frame, text="Upload Manual Well Measurement Sheet",command=lambda: update_manual_data_path(manual_data_path_label, sheets_manager), pady=7)
select_manual_well_data_button.pack()


generate_sheet_button = Button(button_frame, text="Generate New Sheet", pady=5)
generate_sheet_button.pack()


test_sheets_button = Button(label_frame, text="Test reading sheets", command=sheets_manager.scrape_manual_sheet,pady=5)
test_sheets_button.pack()
"""

# ------------------------------
# New format testing

"""
 With this window, the user will be given the menu to edit the 
 well data worksheet. The user will have to select the file first. 
 Then they will be given the option to add a new entry. 
 
 Soon the user will be able to add the html data, but I don't know how to 
 process that yet. 
"""
well_data_root = Tk()
well_data_root.geometry("600x600")
well_data_root.title("Well Data Manager")
well_data_root.iconbitmap('logoicon.ico')

# Setup label frame for buttons
well_data_manager_frame = LabelFrame(well_data_root, 
                                     text="Well Data Sheets Manager",
                                     width=500, height=200)
well_data_manager_frame.pack()
well_data_manager_frame.pack_propagate(False)


load_worksheet_button = Button(well_data_manager_frame, 
                               text="Load Well Data Worksheet", 
                               command=None, 
                               pady=5)
load_worksheet_button.pack()

add_new_entry_button = Button(well_data_manager_frame,
                              text="Add new manual entry",
                              command=None,
                              pady=5)
add_new_entry_button.pack()


def main():
    #root.resizable(False, False)
    #root.grid_propagate(False)
    #root.mainloop()
    well_data_root.mainloop()

if __name__ == "__main__":
    main()
