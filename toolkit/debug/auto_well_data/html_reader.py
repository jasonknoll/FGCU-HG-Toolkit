"""
 I don't quite know how I'm going to structure this yet. 
 I'll probably be following some sort for OO microservices approach
 and everything will be OOP based. Not quite as elegant but it gets the
 job done. 
"""

# find some html reader class
# This will read the well HTMl file and spit it into a sheets/excel file
# Probably sheets

class HtmlReader:
    def __init__(self):
        self.curr_file_path = None

    def set_curr_file(self, path):
        self.curr_file_path = path