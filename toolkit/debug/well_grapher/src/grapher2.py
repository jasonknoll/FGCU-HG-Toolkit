"""
 FGCU Hydrogeology Well Data Graph Generator
 Author: Jason knoll
 version: 0.1.6
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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

from kivy.lang import Builder

from kivy.config import Config

from kivy.core.window import Window

# Google api imports 
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

g_scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
sheet_id = '1u8uMAEu6FZPHEoKERau1R_emPtARuAPBbDWfZZvY6Ao'


"""
 Builder allows me to add buttons and features using the Kivy languaged
"""
Builder.load_string("""
<MainMenu>:
    Screen:
        GridLayout:
            cols: 1    
            Label:
                id: test_login_label 
                text: ""
                markup: True

            Button:
                id: test_login_button
                text: "Login"
                on_press: 
                    root.login()


            Button:
                id: test_graph_menu_button
                text: "Graphing"
                on_press: 
                    root.sm.current = 'graph'

<GraphMenu>:
    Screen:
        GridLayout:
            cols: 1
            Label:
                text: "Test text"
            CheckBox:
                id: sevenA
""")


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
     Constructs the resource api necessary to access google sheets
     @return google's api service for google sheets
    """
    @staticmethod
    def build_sheets_service(creds):
        try:
            return build('sheets', 'v4', credentials=creds).spreadsheets()
        except HttpError as err:
            print(err)


"""
 + GraphGenerator
 The graph genertor object will take in which sheets and colors have been selected by the GUI
 and parse those sheets. The data will be inserted into pandas dataframes which will
 allow for easier working with matplotlib.
"""
class GraphGenerator:
    def __init__(self):
        """
         Init google api service
         This allows the graph generator object to 
        """

        self.goog = GoogleHandler()

        self.sheet = self.goog.build_sheets_service(self.goog.connect_to_google(g_scopes)) 
   
    def generate(self):
        pass


"""
 Graphing menu window

 TODO Using kivy.builder, set this to another grid layout
"""
class GraphMenu(Screen):
    def __init__(self, *args, **kwargs):
        super(GraphMenu, self).__init__(*args, **kwargs)

        self.gen = GraphGenerator()

        self.ids.sevenA.bind(active=self.test_check_box)


    def test_check_box(self, cb, value):
        if value:
            print("checkbox checked")
        else:
            print("unchecked")
"""
 Main menu window 

 TODO using screen manager, set this to one screen with the graphing
 / menu as another. Then using builder, add the necessary widgets.

 Have the label change from false to true when a token is detected.
 Change colors too

# Figure out how to set this up as a screen! 
class MainMenu(Screen):
"""
class MainMenu(Screen):
    def __init__(self, sm, goog=GoogleHandler(), *args, **kwargs):
        super(MainMenu, self).__init__(*args, **kwargs)

        # check for credentials/token to determine this
        # REMOVE THIS FROM CLASS POTENTIALLY
        # SOME OF THESE VARIABLES NEEDS TO BE ACCESSED/EDITED OUTSIDE OF THIS CLASS
        self.logged_in = self.set_login()
        self.login_text_color = self.set_login_text_color()

        self.google = goog

        self.cols = 1
        
        # Screen manager needed to feed to kivy design
        self.sm = sm

        # TODO NEXT Figure out how to update this
        self.logged_in_label = Label(text=f'Connected to Google Sheets: [color={self.login_text_color}]{str(self.logged_in)}[/color]', markup=True)
        
        self.ids.test_login_label.text = f"Login status: [color={self.login_text_color}]{str(self.logged_in)}[/color]"

        # Using kv language, update label
        #self.add_widget(self.ids.test_login_label)

        # Maybe force the user to do this every time
        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.login)
        #self.add_widget(self.ids.test_login_button)

        # On click, open the graphing menu
        self.graph_menu_button = Button(text='Graph menu')
        #self.add_widget(self.ids.test_graph_menu_button)

    # Probably not very useful for setting the variable
    # @return Bool: token.json exists
    def set_login(self):
        print(f"{str(os.path.exists('../creds/token.json'))}")
        return os.path.exists('../creds/token.json')

    """
     Used by the button to actually login using the global scopes variable
    """
    def login(self):
        self.google.connect_to_google(g_scopes)
        self.logged_in = self.set_login()
        self.set_login_text_color()

    """
     Just changes from green to red. Will have to be called again
     if not logged in initially, and the label will need to be updated
    """
    def set_login_text_color(self):

        if self.logged_in:
            self.set_login_text(green_text_color)
            print("pl")
            return  green_text_color
        else:
            self.set_login_text(red_text_color)
            return red_text_color

    def set_login_text(self, color):
        self.ids.test_login_label.text = f"Login status: [color={color}]{str(self.logged_in)}[/color]"

    """
     May need to be called when the user clicks the
     graphing button
    """
    def switch_to_graphing(self):
        pass

"""
 Main application object used by kivy to run the app
"""
class GraphApp(App):
    def build(self):
        """
         TODO somehow, add both the main and graphing menus to sm, and add all 
         / necessary widgets. 
        """

        sm = ScreenManager()

        main_menu = MainMenu(sm, name='')

        sm.add_widget(MainMenu(sm, name='main'))
        sm.add_widget(GraphMenu(name='graph'))
        Window.size = (480, 480)
        self.title = 'FGCU Hydrogeology Graph Generator'
        return sm


def main():
    GraphApp().run()

if __name__ == '__main__':
    main()