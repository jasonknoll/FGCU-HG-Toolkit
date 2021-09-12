#import openpyxl

from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

# Constant path to 
PATH_TO_SHEETS = "../test"

def save_workbook(wb, name):
    wb.save(f"{PATH_TO_SHEETS}/{name}")

def print_cell_value(ws, cell):
    print(ws[f'{cell}'].value)

def set_cell_value(ws, cell, val=""):
    ws[f'{cell}'].value = val

def main():
    # Get outselved a workbook
    wb = Workbook()

    # get the active worksheet
    selected_ws = wb.active

if __name__ == "__main__":
    main()