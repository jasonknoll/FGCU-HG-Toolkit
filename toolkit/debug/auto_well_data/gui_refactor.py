import tkinter.filedialog
import tkinter as tk
from tkinter import *

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
    def __init__(self, size="600x600", title="", icon=None):
        super().__init__(size, title, icon)
    
    def setup_frames(self):
        load_worksheet_frame = LabelFrame(self.root, 
                                          text="Well Data Sheets Manager",
                                          width=500,
                                          height=200)
        data_entry_frame = LabelFrame(self.root, text="")
    
def main():
    pass

if __name__ == "__main__":
    main()