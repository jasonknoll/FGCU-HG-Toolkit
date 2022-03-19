'''
 This is the main file which houses the GUI and main loop
'''

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

from kivy.properties import ObjectProperty


class GraphMenu(Screen): 
    ''' 
     This is the class for the object which contains all UI data for the graph menu GUI
    '''
    pass

class LoginMenu(Screen): 
    pass

if __name__ == '__main__':
    pass