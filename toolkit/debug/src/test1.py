# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 00:35:25 2021

@author: jason
"""

"""
 - TEST 1 - Intro 
 
 + First test: edit cells requested by player
 + Create, save, open, close workbooks
 + edit/remove/create sheets
 
 This is essentially just so I can practice working with excel until I 
 get access to the specific details of the project's process again.
"""

from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter 

def create_new_workbook(title=""):
    new_wb = Workbook()
    
    # TODO check if a title has been set
    # if not, it'll get some default name
    # that I'll set later
    
    return new_wb


def main():
    pass

if __name__ == "__main__":
    main()