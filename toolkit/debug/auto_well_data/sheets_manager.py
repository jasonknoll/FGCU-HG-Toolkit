"""
 Manage the sheets' information
 including handling both old and new data,
 compiling data, and running the corrections on the
 depths. Afterward a new sheet will be generated
"""

import pandas as pd
from openpyxl import Workbook, load_workbook


class SheetsManager:
    def __init__(self, s1=None, s2=None):
        # old and new sheets needing to be compiled together
        self.manual_data_path = s1
        self.existing_well_data = s2
        self.new_sheet = None
        
        self.manual_wb = None
        
        # Pandas dataframes
        self.wells = []

        
    def set_manual_data_path(self, sheet):
        self.manual_data_path = sheet
        
    def get_manual_data_path(self):
        return self.manual_data_path
            
    
    # TODO read all data from the manual entries
    def scrape_manual_sheet(self):
        # First it'll scrape all the sheets to get the wells and create our well objects
        self.manual_wb = pd.ExcelFile(self.get_manual_data_path())
        
        # Create our well objects from file without creating duplicates
        
        for s in self.manual_wb.sheet_names:
            self.wells.append(pd.read_excel(self.manual_wb, s))
            #self.wells.append(pd.read_excel(self.get_manual_data_path(), sheet_name=s))
            # Maybe have a popup window showing progress?? 
            
        #print(self.wells[0].head()) 
        #print(self.wells[0]['7A I (mm)'])
        
            
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
        
