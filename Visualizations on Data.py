import pandas as pd
import matplotlib.pyplot as plt
from dataImport import openTXT, thisIsMyOpenCSVFunctionItsReallyGreat as oCSV

air_data = oCSV("air_quality_no2_long.csv")

print(air_data.head())
air_data.plot(x='date.utc', y='value')
plt.title("Air Quality Data in Paris")
plt.xlabel("Date")
plt.ylabel("Measurement Value of data is micrograms/m^3")
plt.show()
