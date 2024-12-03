import pandas as pd
import numpy as np
df = pd.read_csv('AQI_Data.csv')

a = df.head(5)
# print( "First 5 rows of dataset df are:",a)

b=df.tail(6)
# print("Last rows of dataset df are:",b)

c=df.describe()
# print(c)

fifth_part = df.groupby('City').agg(
    AQI_mean=('AQI', 'mean'),
    PM25_mean=('PM2.5', 'mean'),
    PM10_mean=('PM10', 'mean')
).reset_index()

print("mean of the given parameter of all the cities\n",fifth_part)