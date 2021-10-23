"""
 Manage the sheets' information
 including handling both old and new data,
 compiling data, and running the corrections on the
 depths. Afterward a new sheet will be generated
"""

import pandas as pd
from openpyxl import Workbook, load_workbook

"""
 TODO Get Lane's advice so that I can compile all the data
 correctly. I have the data stripped, but now I have to manipulate it.
"""

class SheetsManager:
    def __init__(self, s1=None, s2=None):
        self.manual_data_path = s1
        # "Well measurements on campus"
        self.existing_data_path = s2
        self.new_sheet = None
        
        # Workbooks (which haven't been opened yet)
        self.manual_wb = None
        self.existing_well_wb = None
        
        # Pandas dataframes
        self.manual_well_data = []
        self.existing_well_data = []

        
    def set_manual_data_path(self, sheet):
        self.manual_data_path = sheet
        
    def get_manual_data_path(self):
        return self.manual_data_path
            
    
    # TODO read all data from the manual entries
    def scrape_manual_sheet(self):
        # First it'll scrape all the sheets to get the wells and create our well objects
        self.manual_wb = pd.ExcelFile(self.get_manual_data_path())
        
        # Store a df of every sheet in our list of sheets
        for s in self.manual_wb.sheet_names:
            self.manual_well_data.append(pd.read_excel(self.manual_wb, s))
            #self.wells.append(pd.read_excel(self.get_manual_data_path(), sheet_name=s))
            # Maybe have a popup window showing progress?? 
            
        #print(self.wells[0].head()) 
        #print(self.wells[0]['7A I (mm)'])
        
            
        # TODO search through all the rows and columns and put it all into a 2d list?
        # Create pandas dataframe and work with it?
    
    def set_existing_data_path(self, sheet):
        self.existing_well_data = sheet
        
    def get_existing_data_path(self):
        return self.existing_data_path
    
    def scrape_existing_sheet(self):
        self.existing_well_wb = pd.ExcelFile(self.get_existing_data_path())
        
        for s in self.existing_well_wb.sheet_names:
            self.existing_well_data.append(pd.read_excel(self.existing_well_wb, s))
    
    # TODO Add this for future use (so that it automatically adds the entry for user)
    def add_manual_data_entry(self):
        pass
        
    """
     Combine old and new sheets and do calculations
     for depth and pressure
    """
    def combine_sheets(self):
        pass
    
    # After everything is done, we gotta reupload it to drive
    def upload_to_google():
        pass
        
