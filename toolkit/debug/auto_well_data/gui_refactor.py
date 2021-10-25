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
        
        
        
    def pack_frame(self, frame):
        frame.pack()
        
    def unpack_frame(self, frame):
        frame.pack_forget()


class WellDataGUI(GUI):
    def __init__(self, size="640x480", title="", icon=None, sm=sheets_manager.SheetsManager()):
        super().__init__(size, title, icon)
        self.file_loaded = False
        self.sm = sm
        if (not sm):
            self.sm = sheets_manager.SheetsManager()
     
    # setup the frames needed then add to list of frames (for now just one)
    def setup_frames(self):
        load_worksheet_frame = LabelFrame(self.root, 
                                          text="Well Data Sheets Manager",
                                          width=550,
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
                                      width=550,
                                      height=200)
        self.frames.append(data_entry_frame)
        
        load_worksheet_button = Button(self.frames[0], 
                                       text="Load well data workbook",
                                       command=lambda: self.sm.select_well_data_popup(self),
                                       pady=5)
        self.buttons.append(load_worksheet_button)
        
        load_worksheet_frame.pack()
        load_worksheet_frame.pack_propagate(False)
        
        load_worksheet_button.pack()
        
        spacer.pack()
        
        loaded_worksheet_label.pack()
        
        data_entry_frame.pack_propagate(False)
        
    def check_file_loaded(self):
        if (self.file_loaded):
            self.frames[1].pack()
        else:
            self.frames[1].pack_forget()
    
    
def main():
    window = WellDataGUI()
    window.setup_frames()
    window.root.mainloop()

if __name__ == "__main__":
    main()