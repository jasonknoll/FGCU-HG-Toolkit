"""
 I don't quite know how I'm going to structure this yet. 
 I'll probably be following some sort for OO microservices approach
 and everything will be OOP based. Not quite as elegant but it gets the
 job done. 
"""

# TODO
# Learn how to read the HTML here (or maybe grab the csv somehow)
# Get all the data, but don't export yet until I contact Rotz

class HtmlReader:
    def __init__(self):
        self.curr_file_path = None

    # Getters and setters
    def set_curr_file_path(self, path):
        self.curr_file_path = path
    
    def get_curr_file_path(self):
        return self.curr_file_path
    
    def parse_curr_file(self):
        pass