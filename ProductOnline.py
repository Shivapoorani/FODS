import pandas as pd

sales_data = pd.DataFrame({
    'ProductID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'ProductName': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E',
                     'Product F', 'Product G', 'Product H', 'Product I', 'Product J'],
    'QuantitySold': [100, 150, 120, 200, 80, 170, 90, 130, 110, 160]
})

sorted_sales = sales_data.sort_values(by='QuantitySold', ascending=False)

top_5_products = sorted_sales.head(5)

print("Top 5 Products Sold the Most:")
print(top_5_products[['ProductID', 'ProductName', 'QuantitySold']])
