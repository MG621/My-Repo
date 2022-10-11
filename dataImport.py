# Import various types of data
# use pandas for table data
import pandas as pd

# Write a function that will import text from txt file
# txt file is a "flat" file
# Save it to a string object myText
#   Input: filenmae (or filepath)
#   Return: text

from fileinput import filename

def openTXT(filename):
    with open(filename,'r') as f:
        myText = f.read()
    return myText

# Write a function that will import a table from CSV file
def thisIsMyOpenCSVFunctionItsReallyGreat(filename):
    myDataFrame = pd.read_csv(filename)
    return myDataFrame

# Define a class FileOpener
# in constructor take filename
## Attributes: filename, contents
# will run openCSV or openTXT based on file extension
# constructor: __init__(self):
class FileOpener:
    def __init__(self, filename):
        self.filename = filename
        self.contents = None
        self.fileSelector()

    def fileSelector(self):
        #print the last three characters of filename
        print(self.filename[-3:])
    pass