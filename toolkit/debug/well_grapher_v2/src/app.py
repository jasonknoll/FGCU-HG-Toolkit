'''
 This is the main file which houses the GUI and main loop
'''

import os
import platform

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


# Google functions


class GraphMenu(Screen):
    ''' 
     This is the class for the object which contains all UI data for the graph menu GUI
    '''
    pass


class LoginMenu(Screen):
    '''
     This contains the login menu, which consists of only one widget:
     a button that will call google's login snippet. 

     This screen should be skipped if credentials are valid
    '''
    def __init__(self, *args, **kwargs): 
        # init Screen super class
        super(LoginMenu, self).__init__(*args, **kwargs)


"""
 TODO need to check if the creds are valid. If not,
 delete them and set a `logged_in` variable to false
"""
def delete_creds():
    pass

def check_creds_valid() -> bool:
    '''       
    '''
    pass


class GraphGenerator(App):
    '''
     Kivy object which contains our app widgets
    '''
    sm = ScreenManager()

    # sm.add_widget()


def main():
    GraphGenerator().run()


if __name__ == '__main__':
    pass
