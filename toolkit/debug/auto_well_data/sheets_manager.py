"""
 Manage the sheets' information
 including handling both old and new data,
 compiling data, and running the corrections on the
 depths. Afterward a new sheet will be generated
"""

from openpyxl import Workbook, load_workbook

"""
 TODO Get Lane's advice so that I can compile all the data
 correctly. I have the data stripped, but now I have to manipulate it.
"""

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
    
    def insert_formula_into_reseults_table(self):
        pass
            
    """
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
    """
    
    
"""
    def scrape_existing_sheet(self):
        self.existing_well_wb = pd.ExcelFile(self.get_existing_data_path())
        
        for s in self.existing_well_wb.sheet_names:
            self.existing_well_data.append(pd.read_excel(self.existing_well_wb, s))
    
    # TODO Add this for future use (so that it automatically adds the entry for user)
    def add_manual_data_entry(self):
        pass
"""
        
"""
     Combine old and new sheets and do calculations
"""
        
