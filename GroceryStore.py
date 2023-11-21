import pandas as pd
import numpy as np

df = pd.read_csv('D:\Shiva\FODS\Stores.csv')

quantities = df['Daily_Customer_Count'].to_numpy()
prices = df['Store_Sales'].to_numpy()/quantities 

discount_rate = 0.1 
tax_rate = 0.07

subtotal = np.sum(prices * quantities)

discount = subtotal * discount_rate
subtotal -= discount

tax = subtotal * tax_rate

total = subtotal + tax

print("Subtotal:", subtotal)
print("Discount: ", discount)
print("Tax:", tax)
print("Total:", total)
