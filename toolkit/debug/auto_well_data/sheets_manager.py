"""
 Manage the sheets' information
 including handling both old and new data,
 compiling data, and running the corrections on the
 depths. Afterward a new sheet will be generated
"""

from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from openpyxl import Workbook, load_workbook

from tkinter import filedialog as fd
from tkinter import *

from dateutil import parser


class GoogleManager:
    def __init__(self):
        self.scopes = ['https://www.googleapis.com/auth/spreadsheets']
        self.old_sheet_id = '1RCAEGJuKwnAstDoXLw9eoRIZoJZMe2ZKNsTFyehBaVo'
        self.test_sheet_id = '1u8uMAEu6FZPHEoKERau1R_emPtARuAPBbDWfZZvY6Ao'
        
        """Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('googlesheets/token.json'):
            creds = Credentials.from_authorized_user_file('googlesheets/token.json', self.scopes)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'googlesheets/credentials.json', self.scopes)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('googlesheets/token.json', 'w') as token:
                token.write(creds.to_json())
    
        self.service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        self.sheet = self.service.spreadsheets()
        
        self.well_names = ['22M', '3A', 'MA', 'MM', '5M', 
                           '33M', 'U1', '27M', '6A', '28M', 
                           '29M', '11M', '10M', '7M', '1A', 
                           '9M', '12M', '30M', '5A', '32M', 
                           '31M', '18M', '2A']
        
        # just setting it to the first sheet for now
        self.curr_sheet = self.well_names[0]
        
        """
        self.result = self.sheet.values().get(spreadsheetId=self.test_sheet_id,
                                         range="22M!A2:D13").execute()
        self.values = self.result.get('values', [])
        
        
        print(self.values[0][0]) # A2
        print(self.values[1][0]) # A3
        #print(self.values[20][0]) # A22
        """
        
        
    # Range formatted 'Sheetname!Cell1:Cell2'    
    def update_cell(self, cell_range, value):
        self.sheet.values().update(spreadsheetId=self.test_sheet_id, 
                                   range=cell_range, 
                                   body={'values':[[value]]},
                                   valueInputOption="USER_ENTERED").execute()
        print("updated")
    
    def get_next_empty_row_manual_table(self):
        pass
    
    def get_well_by_name(self, name):
        for well in self.well_names:
            if name == well:
                return well
    
    def setup_dropdown(self, frame):
        
        var = StringVar(frame)
        var.set(self.well_names[0])
        dropdown = OptionMenu(frame, var, *self.well_names)
        
        select_sheet_button = Button(frame, 
                                     command=lambda: self.change_sheet_select(var),
                                     text="Select sheet")
        
        return dropdown, select_sheet_button
    
    def change_sheet_select(self, var):
        self.curr_sheet = self.get_well_by_name(var.get())
        print(self.curr_sheet)
    
class SheetsManager:
    def __init__(self, s1=None):
        self.well_data_path = s1
        self.worksheet_loaded = False
        
        # Workbooks (which haven't been opened yet)
        self.wb = None
        self.curr_sheet = None
        
        self.well_names = []

        
    def set_well_data_path(self, sheet):
        self.well_data_path = sheet
        
    def get_well_data_path(self):
        return self.well_data_path
    
    def select_well_data_popup(self, gui):
        self.set_well_data_path(fd.askopenfilename(filetypes=[("excel files", ".xlsx")]))
        gui.file_loaded = True 
        gui.check_file_loaded()
        self.generate_workbook()
        gui.setup_dropdown(gui.frames[1])
    
    # OpenPyXL functions
    def generate_workbook(self):
        self.wb = load_workbook(self.get_well_data_path())
        self.curr_sheet = self.wb.worksheets[1]
        # setup sheet names (so we can select all the different sheets)
        for i in self.wb.sheetnames[1:len(self.wb.sheetnames)-1]:
            self.well_names.append(i)
            
        print(self.well_names)
        #print(self.curr_sheet['G1'].value)
        
    def save_workbook(self, path):
        self.wb.save(path)
        
    def submit_entry(self, date, time, measure):
        
        date_val = parser.parse(date.get())
        time_val = parser.parse(time.get())
        measure_val = float(measure.get())
        
        next_row = self.get_next_empty_row_manual_table()
        self.insert_manual_data_into_row(date_val, time_val, measure_val, next_row)
        self.insert_formula_into_reseults_table(next_row)
        self.save_workbook(self.get_well_data_path())
        
        
        date.delete(0, END)
        time.delete(0, END)
        measure.delete(0, END)
        
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