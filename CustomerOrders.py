import pandas as pd
import numpy as np

df = pd.read_csv('D:\Shiva\FODS\orders.csv', encoding='latin-1')

orders_per_cust = df.groupby('buyer')['order_no'].count().reset_index(name='total_orders')

avg_qty = df.groupby('sku')['quantity'].mean().reset_index(name='avg_qty')

earliest_date = df['order_date'].min()
latest_date = df['order_date'].max()

print(orders_per_cust)
print(avg_qty)
print("Earliest:", earliest_date)  
print("Latest:", latest_date)
