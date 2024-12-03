import pandas as pd
import numpy as np

# Load the dataset
fifth_part = ('AQI_Data.csv')
data = pd.read_csv(fifth_part)

# A) Extract and display all rows where the city is "Delhi"
delhi_data = data[data['City'].str.lower() == 'delhi']
print("A) Rows where the city is 'Delhi':")
print(delhi_data)

# B) Display the first 10 rows, showing only the columns 'City', 'AQI', and 'PM2.5'
first_10_rows = data[['City', 'AQI', 'PM2.5']].head(10)
print("\nB) First 10 rows with selected columns:")
print(first_10_rows)

# C) Use NumPy to filter out and display rows where AQI > 300 and PM10 > 200
filtered_data = data[np.logical_and(data['AQI'] > 300, data['PM10'] > 200)]
print("\nC) Rows where AQI > 300 and PM10 > 200:")
print(filtered_data)
