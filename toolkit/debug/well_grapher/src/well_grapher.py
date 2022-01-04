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

 + Figure out how to package
"""

import kivy

from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox

from kivy.config import Config

from kivy.core.window import Window

Config.set('graphics', 'resizable', '0')
Config.write()

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
 + Create a main menu window (maybe do a free float layout?)
"""
class MainMenu(GridLayout):
    def __init__(self, *args, **kwargs):
        super(MainMenu, self).__init__(*args, **kwargs)

        # check for credentials/token to determine this
        self.logged_in = False

        self.cols = 1

        self.logged_in_label = Label(text=f'Connected to Google Sheets: [color={red_text_color}]{str(self.logged_in)}[/color]', markup=True)
        
        # Using kv language, update label
        self.add_widget(self.logged_in_label)

        # Maybe gray-out if logged in already?
        self.add_widget(Button(text='Login'))

        # On click, open the graphing menu
        self.add_widget(Button(text='Graphing'))



"""
 + Create a graphing menu window
"""
class GraphMenu(GridLayout):
    def __init__(self):
        pass


class GraphApp(App):
    def build(self):
        Window.size = (640, 480)
        self.title = 'FGCU Hydrogeology Graph Generator'
        return MainMenu()

if __name__ == '__main__':
    GraphApp().run()