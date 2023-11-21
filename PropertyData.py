import pandas as pd
import numpy as np

df = pd.read_csv('D:/Shiva/FODS/property_data.csv')

average_price_per_location_pandas = df.groupby('location')['listing price'].mean()
print("Average Listing Price in Each Location:")
print(average_price_per_location_pandas)

df['number of bedrooms'] = pd.to_numeric(df['number of bedrooms'], errors='coerce')

num_properties_more_than_four_bedrooms = np.sum(df['number of bedrooms'] > 4)
print(f"\nNumber of Properties with More Than Four Bedrooms: {num_properties_more_than_four_bedrooms}")

df['area in square feet'] = pd.to_numeric(df['area in square feet'], errors='coerce')

df = df.dropna(subset=['area in square feet'])

if not df.empty:
    property_with_largest_area_pandas = df.loc[df['area in square feet'].idxmax()]
    print("\nProperty with the Largest Area (Pandas):")
    print(property_with_largest_area_pandas)
else:
    print("No data remaining after dropping NaN values.")


