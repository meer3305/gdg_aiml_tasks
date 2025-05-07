# Day 2 - AI/ML Class: Linear Regression and K-Means on Iris Dataset

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

# Load the dataset
df = pd.read_csv('Sneakers.csv')

# ========== PART 1: LINEAR REGRESSION ==========

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

# ---------- LINEAR REGRESSION ----------

# Use avg_width to predict avg_height
X_lr = df[['avg_width']]
y_lr = df['avg_height']

# Create and fit linear regression model
lr_model = LinearRegression()
lr_model.fit(X_lr, y_lr)
y_pred = lr_model.predict(X_lr)

# Plot Linear Regression
plt.figure(figsize=(8, 5))
plt.scatter(X_lr, y_lr, color='blue', label='Actual Data')
plt.plot(X_lr, y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel('Average Width')
plt.ylabel('Average Height')
plt.title('Linear Regression: avg_width vs avg_height')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------- K-MEANS CLUSTERING ----------

# Use avg_width and avg_height for clustering
X_kmeans = df[['avg_width', 'avg_height']]
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_kmeans)
df['Cluster'] = kmeans.labels_

# Plot Clusters
plt.figure(figsize=(8, 5))
colors = ['red', 'green', 'blue']
for i in range(3):
    cluster_data = df[df['Cluster'] == i]
    plt.scatter(cluster_data['avg_width'], cluster_data['avg_height'], color=colors[i], label=f'Cluster {i}')

# Plot centroids
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], s=200, marker='x', c='black', label='Centroids')

plt.xlabel('Average Width')
plt.ylabel('Average Height')
plt.title('K-Means Clustering: avg_width vs avg_height')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()