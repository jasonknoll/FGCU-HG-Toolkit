"""
 Manage the sheets' information
 including handling both old and new data,
 compiling data, and running the corrections on the
 depths. Afterward a new sheet will be generated
"""

import pandas as pd
from openpyxl import Workbook, load_workbook

# Create objects for every well to organize the data a little better
class Well:
    def __init__(self, name=''):
        self.name = name
        self.isAutomatic = False
        if (self.name[-1].upper() == 'A'):
            self.isAutomatic = True
            

class SheetsManager:
    def __init__(self, s1=None, s2=None):
        # old and new sheets needing to be compiled together
        self.manual_data = s1
        self.existing_well_data = s2
        self.new_sheet = None
        
        self.curr_wb = None
        
        self.wells = []
        
        # pandas splits all the dataframes into sheets for us? https://www.sitepoint.com/using-python-parse-spreadsheet-data/
        self.sheets = []
        
    def set_manual_data_path(self, sheet):
        self.manual_data = sheet
        
    def get_manual_data_path(self):
        return self.manual_data
    
    def check_if_well_exists(self, well_name) -> bool:
        for w in self.wells:
            if (w.name != well_name):
                    continue
            else:
                return True
        return False
            
    
    # TODO read all data from the manual entries
    def scrape_manual_sheet(self):
        # First it'll scrape all the sheets to get the wells and create our well objects
        self.curr_wb = load_workbook(self.get_manual_data_path())
        
        # Create our well objects from file without creating duplicates
        for s in self.curr_wb.sheetnames:
            if (not self.check_if_well_exists(s)):
                self.wells.append(Well(s))
                
        print(self.curr_wb[self.wells[0].name]['A1'].value)
            
        # TODO search through all the rows and columns and put it all into a 2d list?
        # Create pandas dataframe and work with it?
        
    """
     Combine old and new sheets and do calculations
     for depth and pressure
    """
    def combine_sheets(self):
        pass
    
    # After everything is done, we gotta reupload it to drive
    def upload_to_google():
        pass
        
