"""
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
"""

import kivy

from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput 
from kivy.uix.gridlayout import GridLayout


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
 + Create a main menu window
"""
class MainMenu(GridLayout):
    def __init__(self):
        super(MainMenu, self).__init__(*args, **kwargs)

        # check for credentials/token to determine this
        self.loggedIn = False

        self.cols = 2
        
        # Using kv language, update label
        self.add_widget(Label(text=f'Connected to Google Sheets: {str(self.loggedIn)}'))

        # 
        self.add_widget(Button(text='Login')))

"""
 + Create a graphing menu window
"""
class GraphMenu(GridLayout):
    def __init__(self):
        pass


def main():
    pass

if __name__ == '__main__':
    main()