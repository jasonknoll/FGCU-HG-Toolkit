"""
 Handle the GUI and interactions
 with the user
"""
import tkinter as tk
from tkinter import *, ttk

# TODO Setup window size
# Add buttons and shit
# Figure out how to select files from HD
# connect to Google Sheet API

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
TITLE = "Hydrogeology Well Data Processor v0.1"

# I have to setup a canvas or something

class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

# Combine old data with the newly generated sheet
def combine_sheets(sheet1, sheet2):
    pass

def select_file():
    pass

def draw_window():
    pass

def main():
    # initialize window
    gui = GUI()
    gui.master.title(TITLE)
    gui.master.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)

if __name__ == "__main__":
    main()
