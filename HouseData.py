import numpy as np

house_data = np.array([
    [3, 1500, 200000],
    [4, 1800, 250000],
    [5, 2000, 300000],
    [4, 1600, 220000]
])

filtered_prices = house_data[house_data[:, 0] > 4][:, -1]

average_price = np.mean(filtered_prices)

print("Average Sale Price of Houses with More Than Four Bedrooms:", average_price)
