"""
 Handle the GUI and interactions
 with the user.
 Will be the main executable
"""

import tkinter.filedialog
import tkinter as tk
from tkinter import *

import html_reader as hr

import sheets_manager

from dateutil import parser


"""
root = Tk()
root.geometry("640x480")
root.tit"le("HG-Well-Data-Toolkit v0.1")
root.iconbitmap('logoicon.ico')
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

new_entry_root = None

sm = sheets_manager.SheetsManager()

def load_well_data_worksheet(sm):
    sm.set_well_data_path(tkinter.filedialog.askopenfilename(filetypes=[("excel files", ".xlsx")]))
    if (sm.get_well_data_path()):
        add_new_entry_button['state'] = "active"

# Setup label frame for buttons
well_data_manager_frame = LabelFrame(well_data_root, 
                                     text="Well Data Sheets Manager",
                                     width=500, height=200)
well_data_manager_frame.pack()
well_data_manager_frame.pack_propagate(False)


load_worksheet_button = Button(well_data_manager_frame, 
                               text="Load Well Data Worksheet", 
                               command=lambda: load_well_data_worksheet(sm), 
                               pady=5)
load_worksheet_button.pack()

"""
 Now this function needs to take the data from the entries
 and spit it into the loaded sheet.
 
 1. Find the next row in the manual table
 2. Insert data
 3. Insert formula to corresponding row in the results table
"""

    

# TODO Refactor ALL of this code lmao
# This needs to go into a window class or something
def setup_new_entry_window_labels(new_entry_root, frame, sm=sm):
    # TODO create a dropdown to select sheet
    
    date_label = Label(frame, text="Date (mm/dd/yy)", anchor="w", justify=LEFT)
    date_label.pack()
    
    date_entry = Entry(frame, bd=3)
    date_entry.pack()
    
    time_label = Label(frame, text="Time (hh:mm AM)")
    time_label.pack()
    
    time_entry = Entry(frame, bd=3)
    time_entry.pack()
    
    i_measurement_label = Label(frame, text="Internal water level (mm)")
    i_measurement_label.pack()
    
    i_measurement_entry = Entry(frame, bd=3)
    i_measurement_entry.pack()
    
    submit_button = Button(frame, 
                           text="Submit entry",
                           command=lambda: handle_workbook(sm, date_entry, time_entry, i_measurement_entry), 
                           pady=5)
    submit_button.pack()
    
    exit_button = Button(frame, text="Exit", command=new_entry_root.destroy, pady=5)
    exit_button.pack()

def create_new_entry_window(size="400x400", title="New Manual Data Entry", icon="logoicon.ico"):
    new_entry_root = Tk()
    new_entry_root.geometry(size)
    new_entry_root.title(title)
    new_entry_root.iconbitmap(icon)
    
    entry_label_frame = LabelFrame(new_entry_root,
                                   text="New Manual Data Entry",
                                   width=350,
                                   height=350,
                                   bd=4)
    entry_label_frame.pack()
    entry_label_frame.pack_propagate(False)
    
    # Add labels and stuff
    setup_new_entry_window_labels(new_entry_root, entry_label_frame)
    
    new_entry_root.mainloop()

add_new_entry_button = Button(well_data_manager_frame,
                              text="Add new manual entry",
                              command=create_new_entry_window,
                              pady=5)
add_new_entry_button.pack()
# can't add an entry to a file that isn't loaded yet
add_new_entry_button['state'] = "disabled"


# TODO REFACTOR!
# TODO Add ability to select which sheet we're editing

def main():
    #root.resizable(False, False)
    #root.grid_propagate(False)
    #root.mainloop()
    well_data_root.mainloop()

if __name__ == "__main__":
    main()
