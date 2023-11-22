import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'TotalAmountSpent': [100, 300, 150, 500, 200, 600, 350, 800, 400, 700],
    'FrequencyOfVisits': [2, 4, 3, 5, 2, 6, 4, 8, 3, 7]
}
df = pd.DataFrame(data)

X = df[['TotalAmountSpent', 'FrequencyOfVisits']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

num_clusters = 3

kmeans_model = KMeans(n_clusters=num_clusters, random_state=42)
df['Cluster'] = kmeans_model.fit_predict(X_scaled)

plt.scatter(df['TotalAmountSpent'], df['FrequencyOfVisits'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Total Amount Spent')
plt.ylabel('Frequency of Visits')
plt.title('Customer Segmentation with K-Means Clustering')
plt.show()

cluster_centers = scaler.inverse_transform(kmeans_model.cluster_centers_)
cluster_centers_df = pd.DataFrame(cluster_centers, columns=['TotalAmountSpent', 'FrequencyOfVisits'])
print("Cluster Centers:")
print(cluster_centers_df)
