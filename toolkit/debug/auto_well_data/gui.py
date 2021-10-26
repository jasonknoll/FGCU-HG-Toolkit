import tkinter.filedialog
import tkinter as tk
from tkinter import *

import sheets_manager

"""
 This file is a reorganization of the original gui.py
 as that code was super messy. They should function identically.
"""

class GUI:
    def __init__(self, size="600x600", title="", icon=None):
        self.window_size = size
        self.window_title = title
        self.window_icon = icon
        
        # Initialize the window
        self.root = Tk()
        self.root.geometry(self.window_size)
        self.root.title(self.window_title)
        self.root.iconbitmap(self.window_icon)
        
        self.frames = []
        self.labels = []
        self.buttons = []
    


class WellDataGUI(GUI):
    def __init__(self, size="640x370", title="", icon=None, sm=sheets_manager.SheetsManager()):
        super().__init__(size, title, icon)
        self.file_loaded = False
        self.sm = sm
        if (not sm):
            self.sm = sheets_manager.SheetsManager()
     
    # setup the frames needed then add to list of frames (for now just one)
    def setup_frames(self):
        load_worksheet_frame = LabelFrame(self.root, 
                                          text="Well Data Sheets Manager",
                                          width=570,
                                          height=150)
        self.frames.append(load_worksheet_frame)
        
        spacer = Label(load_worksheet_frame,
                       text="",
                       pady=3)
        
        loaded_worksheet_label = Label(load_worksheet_frame, 
                                       text="Loaded excel sheet: none",
                                       pady=3,
                                       wraplength=400)
        
        data_entry_frame = LabelFrame(self.root,
                                      text="Enter Manual Data",
                                      width=570,
                                      height=200)
        self.frames.append(data_entry_frame)
        
        load_worksheet_button = Button(self.frames[0], 
                                       text="Load well data workbook",
                                       command=lambda: self.sm.select_well_data_popup(self),
                                       pady=5)
        self.buttons.append(load_worksheet_button)
        
        
        # ----- setup labels and text entries -----
        
        
        
        date_label = Label(data_entry_frame, 
                           text="Date (mm/dd/yy)", 
                           justify=CENTER,)
        date_label.grid(column=0, row=1)
        
        date_entry = Entry(data_entry_frame, bd=3)
        date_entry.grid(column= 0, row=2)
        
        
        time_label = Label(data_entry_frame, text="Time (hh:mm AM)")
        time_label.grid(column=1, row=1)
        
        time_entry = Entry(data_entry_frame, bd=3)
        time_entry.grid(column=1, row=2)
        
        
        measure_label = Label(data_entry_frame, text="Internal water level (mm)")
        measure_label.grid(column=2, row=1)
        
        measure_entry = Entry(data_entry_frame, bd=3)
        measure_entry.grid(column=2, row=2)
        
        
        submit_button = Button(data_entry_frame, 
                               text="Submit entry",
                               command=lambda: self.sm.submit_entry(date_entry, time_entry, measure_entry), 
                               pady=5)
        submit_button.grid(column=0, row=3)
        
        submit_success_label = None
        
        # Diplay default view
        load_worksheet_frame.pack()
        load_worksheet_frame.pack_propagate(False)
        
        load_worksheet_button.pack()
        
        spacer.pack()
        
        loaded_worksheet_label.pack()
        
        data_entry_frame.grid_propagate(False)
        data_entry_frame.grid_columnconfigure(0, minsize=190)
        data_entry_frame.grid_columnconfigure(1, minsize=190)
        data_entry_frame.grid_columnconfigure(2, minsize=190)
        
        data_entry_frame.grid_rowconfigure(0, minsize=50)
        data_entry_frame.grid_rowconfigure(1, minsize=30)
        data_entry_frame.grid_rowconfigure(2, minsize=30)
        data_entry_frame.grid_rowconfigure(3, minsize=50)
        
    def check_file_loaded(self):
        if (self.file_loaded):
            self.frames[1].pack()
        else:
            self.frames[1].pack_forget()
            
    def update_file_path_label(self):
        pass
    
    def setup_dropdown(self, frame):
        var = StringVar(frame)
        var.set(self.sm.well_names[0])
        dropdown = OptionMenu(frame, var, *self.sm.well_names)
        dropdown.grid(column=0, row=0)
        
        select_sheet_button = Button(frame, 
                                     command=lambda: self.change_sheet_select(var),
                                     text="Select sheet")
        select_sheet_button.grid(column=1, row=0)
        
        return dropdown
    
    def change_sheet_select(self, var):
        self.sm.curr_sheet = self.sm.wb[f'{var.get()}']
        print(self.sm.curr_sheet)
    
    
def main():
    window = WellDataGUI(title="Hydrogeology Well Data Processor v0.5",
                         icon='logoicon.ico')
    window.setup_frames()
    
    googleman = sheets_manager.GoogleManager()
    window.root.mainloop()
    
    

if __name__ == "__main__":
    main()