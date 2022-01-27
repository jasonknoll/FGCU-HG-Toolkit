"""
 FGCU Hydrogeology graph generator 
 Author: Jason Knoll
"""

# Imports
import pandas as pd

from typing import List


# Module functions
"""
 generate_graph
 
 @desc: 
 @return:
"""
def generate_graph(df: List[pd.DataFrame]):
    pass

"""
 get_last_row (google sheets)
 
 @desc: Find the last row in the sheet
 @return: index of the next row available in the sheet
"""
def get_last_row(sheet, well):
    rows = sheet.values().get(spreadsheetId=sheet_id,
                            range=f"{well}!A1:200").execute()
    data = rows.get('values')

    return len(data)+1

"""
 create_dfs_from_sheets

 @desc: From google sheets, generate dataframes that will be used to generate graphs
 @return: list of dataframes
"""
def create_dfs_from_sheet():
    pass