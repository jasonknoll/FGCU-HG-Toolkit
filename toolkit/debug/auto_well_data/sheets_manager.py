"""
 Manage the sheets' information
 including handling both old and new data,
 compiling data, and running the corrections on the
 depths. Afterward a new sheet will be generated
"""

import openpyxl 
from openpyxl import Workbook

class SheetsManager:
    def __init__(self, s1=None, s2=None):
        self.sheet1 = s1
        self.sheet2 = s2
        self.new_sheet = None
        
    """
     Combine old and new sheets and do calculations
     for depth and pressure
    """
    def combine_sheets(self):
        pass
    
    # After everything is done, we gotta reupload it to drive
    def upload_to_google():
        pass
        
