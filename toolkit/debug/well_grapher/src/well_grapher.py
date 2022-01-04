"""
 FGCU Hydrogeology Well Data Graph Generator
 Author: Jason Knoll
 Version: 0.1.1
"""

"""
 TODO List
 In here, I need to:
 + Refactor well data entry folder
 + Create a main menu window 
    - Add google login status
    - Add login button
    - Add Graphing button (opens new 'Graphing' window)

 + Create graphing menu window
    - Select sheets (checkbox)
    - Select colors (rgb?)

 + Generate graph with selected settings

 + Figure out how to package
"""

import os.path

import kivy

from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox

from kivy.config import Config

from kivy.core.window import Window

import gspread

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


# Prevent the window from being resized
Config.set('graphics', 'resizable', '0')
Config.write()

# Green and red hex values for label text
red_text_color = 'ff0000'
green_text_color = '00ff00'


"""
 + GraphGenerator
 The graph genertor object will take in which sheets and colors have been selected by the GUI
 and parse those sheets. The data will be inserted into pandas dataframes which will
 allow for easier working with matplotlib.
"""
class GraphGenerator:
    def __init__(self):
        pass
    
    def generate(self):
        pass


"""
 Main menu window (maybe do a free float layout?)
"""
class MainMenu(GridLayout):
    def __init__(self, *args, **kwargs):
        super(MainMenu, self).__init__(*args, **kwargs)

        # check for credentials/token to determine this
        # REMOVE THIS FROM CLASS POTENTIALLY
        # SOME OF THESE VARIABLES NEEDS TO BE ACCESSED/EDITED OUTSIDE OF THIS CLASS
        self.logged_in = False

        self.cols = 1

        self.logged_in_label = Label(text=f'Connected to Google Sheets: [color={red_text_color}]{str(self.logged_in)}[/color]', markup=True)
        
        # Using kv language, update label
        self.add_widget(self.logged_in_label)

        # Maybe gray-out if logged in already?
        self.add_widget(Button(text='Login'))

        # On click, open the graphing menu
        self.add_widget(Button(text='Graph Menu'))

    def set_login(self):
        return not self.loggin_in



"""
 Graphing menu window
"""
class GraphMenu(GridLayout):
    def __init__(self):
        pass


"""
 Main application object used by kivy to run the app
"""
class GraphApp(App):
    def build(self):
        Window.size = (640, 480)
        self.title = 'FGCU Hydrogeology Graph Generator'
        return MainMenu()


"""
 The google handler object will handle all data involved with Google api
 authentication and return the data for our sheets. The data will then be passed to the
 graph generator.
"""
class GoogleHandler:
    """
     Create credentials and give permission to access google api
     @return creds
    """
    @staticmethod
    def connect_to_google(scopes):
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
     Constructs the resource api necessary to access google sheets
     @return google's api service for google sheets
    """
    @staticmethod
    def build_sheets_service(creds):
        return build('sheets', 'v4', credentials=creds).spreadsheets()


def main():
    scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    sheet_id = '1u8uMAEu6FZPHEoKERau1R_emPtARuAPBbDWfZZvY6Ao'
    #creds = None

    goog = GoogleHandler()
    
    # This needs to be completed when the user hits 'login' (i think)
    #creds = goog.connect_to_google(scopes)
    #service = goog.build_sheets_service(creds)

    GraphApp().run()

if __name__ == '__main__':
    main()