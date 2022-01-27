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
 get_last_row
 
 @desc: Find the last row in the sheet
 @return: index of the next row available in the sheet
"""
def get_last_row(self, well):
    rows = self.sheet.values().get(spreadsheetId=sheet_id,
                            range=f"{well}!A1:200").execute()
    data = rows.get('values')

    return len(data)+1