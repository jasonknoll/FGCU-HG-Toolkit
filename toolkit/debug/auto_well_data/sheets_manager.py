"""
 Manage the sheets' information
 including handling both old and new data,
 compiling data, and running the corrections on the
 depths. Afterward a new sheet will be generated
"""

from openpyxl import Workbook, load_workbook

from tkinter import filedialog as fd


class SheetsManager:
    def __init__(self, s1=None):
        self.well_data_path = s1
        self.worksheet_loaded = False
        
        # Workbooks (which haven't been opened yet)
        self.wb = None
        self.curr_sheet = None

        
    def set_well_data_path(self, sheet):
        self.well_data_path = sheet
        
    def get_well_data_path(self):
        return self.well_data_path
    
    def select_well_data_popup(self, gui):
        self.set_well_data_path(fd.askopenfilename(filetypes=[("excel files", ".xlsx")]))
        gui.file_loaded = True 
        gui.check_file_loaded()
    
    # OpenPyXL functions
    def generate_workbook(self):
        self.wb = load_workbook(self.get_well_data_path())
        self.curr_sheet = self.wb.worksheets[1]
        #print(self.curr_sheet['G1'].value)
        
    def save_workbook(self, path):
        self.wb.save(path)
        
    def get_next_empty_row_manual_table(self):
        for cell in self.curr_sheet['G']:
            if not cell.value:
                return cell.row
    
    def insert_manual_data_into_row(self, date, time, measure, row):
        self.curr_sheet[f'G{row}'].value = date
        self.curr_sheet[f'H{row}'].value = time
        self.curr_sheet[f'I{row}'].value = measure
    
    def insert_formula_into_reseults_table(self, row):
        self.curr_sheet[f'A{row}'].value = f"=G{row}"
        self.curr_sheet[f'B{row}'].value = f"=H{row}"
        self.curr_sheet[f'C{row}'].value = f"=D{row}/305"
        self.curr_sheet[f'C{row}'].number_format = '0.00'
        self.curr_sheet[f'D{row}'].value = f"=I{row}"