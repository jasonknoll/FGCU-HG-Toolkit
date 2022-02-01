"""
 FGCU Hydrogeology graph generator API
 Author: Jason Knoll
"""

# Imports
import pandas as pd

from typing import List

from googleapiclient.discovery import build 
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transports.requests import Request
from google.oauth2.credentials import Credentials


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

# Google functions
"""
 setup_google_creds

 @desc: Create credentials and set up permissions
 @return: creds (google object idk)
"""
def setup_google_creds(scopes):
    creds = ""
    if os.path.exists('../creds/token.json'):
        creds = Credentials.from_authorized_user_file('../creds/token.json', scopes)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '../creds/credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('../creds/token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

"""
 build_sheets_service(creds)

 @desc: from credentials, build the google api sheets service
 object
 
 @return: sheets service
"""

def build_sheets_service(creds):
    try:
        return build('sheets', 'v4', credentials=creds)
    except HttpError as err:
        print(err)