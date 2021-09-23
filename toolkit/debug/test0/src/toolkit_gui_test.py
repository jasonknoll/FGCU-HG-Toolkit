# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:57:47 2021

@author: jason
"""

from tkinter import *
from tkinter import ttk

from openpyxl import Workbook, load_workbook 


"""
 TODO everything 
 + big buttons for sheet control
     - create
     - open
     - save 
 + if sheet is open, have buttons/menu to edit cells
 + deal with the *event binding*
"""

# Main loop will hold my "global" varaibles
def main():
    # Blank default workbook
    current_wb = Workbook()
    current_ws = current_wb.active
    
    # TODO open window (non-adjustable to start)
    
    
    # "Obligatory first program"
    root = Tk()
    
    # button setup? 
    buttons = []
    ttk.Button(root, text="Hello WOrld").grid()
    
    root.mainloop()
    
    
if __name__ == '__main__':
    main()