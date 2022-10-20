# Part 1
import pandas as pd
from dataImport import openTXT, thisIsMyOpenCSVFunctionItsReallyGreat as oCSV

# Part 2
myDF = oCSV("bestsellers.csv")
print(myDF.info())
print("There are 550 entries")
print("Columns contain things such as name, author, ratings, reviews, price, year, and genre")
print("There are objects, floating numbers, and integers")
print("There are no missing entries in the entire dataframe")

# Part 3
print("================================================Displaying the first five rows================================================")
print(myDF.head())
print("=====================================================Displaying ten rows======================================================")
print(myDF.head(10))
#authors = myDF["Author"]
print("==================================================Displaying only five authors================================================")
print(myDF['Author'].head())

# Part 4
# Most expensive
#mostExpensive = myDF.sort_values(by='Price', ascending=False)
#mostExpensive = mostExpensive['Price'].iloc[0]
#print(f"The most expensive price is {mostExpensive}")
print(f"The most expensive price is {myDF['Price'].max()}")
print(f"The lowest user rating is {myDF['User Rating'].min()}")
print(f"There are {myDF['Year'].max()-myDF['Year'].min()} years of data in this dataframe")
print(f"The average price is {myDF['Price'].mean()}")
print(f"There are {myDF['Author'].nunique()} unique authors")