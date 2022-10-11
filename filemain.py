# load the dataImport functions
# load thisIsMyOpenCSVFunctionItsReallyGreat with an alias

#call the openTXT() function

from dataImport import openTXT
from dataImport import FileOpener
from dataImport import thisIsMyOpenCSVFunctionItsReallyGreat as oCSV

result = openTXT("text.txt")
print(result)

# call the openCSV() function
myDF = oCSV("titanic.csv")
# .head() prints the first 5 rows of the table
print(myDF.head())
# .info() will show some details on the dataset
print(myDF.info())

myFO = FileOpener("titanic.csv")