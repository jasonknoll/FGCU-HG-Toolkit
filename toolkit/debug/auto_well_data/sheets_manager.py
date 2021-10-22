"""
 Manage the sheets' information
 including handling both old and new data,
 compiling data, and running the corrections on the
 depths. Afterward a new sheet will be generated
"""

import openpyxl 
from openpyxl import Workbook

# Create objects for every well to organize the data a little better
class Well:
    def __init__(self):
        pass

class SheetsManager:
    def __init__(self, s1=None, s2=None):
        # old and new sheets needing to be compiled together
        self.manual_data = s1
        self.existing_well_data = s2
        self.new_sheet = None
        
        self.scraped_manual_data = []
        self.wells = []
        
    def set_manual_sheet(self, sheet):
        self.manual_data = sheet
        
    def get_manual_sheet(self):
        return self.manual_data
    
    # TODO read all data from the manual entries
    def scrape_manual_sheet(self):
        # First it'll scrape all the sheets to get the wells and create our well objects
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
        
