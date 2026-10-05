"""
Retail Customer Segmentation using K-Means
Minor Project
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

# 1. Load data
df = pd.read_csv("../data/retail_customer_data.csv")

# 2. Select clustering features
features = [
    "AnnualIncome",
    "PurchaseFrequency",
    "AvgOrderValue",
    "TotalSpend",
    "RecencyDays",
    "DiscountUsagePct"
]

X = df[features]

# 3. Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Find a suitable K using silhouette score
scores = {}
for k in range(2, 7):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(X_scaled)
    scores[k] = silhouette_score(X_scaled, labels)

best_k = max(scores, key=scores.get)
print("Best K:", best_k)
print("Silhouette scores:", scores)

# 5. Train final K-Means model
kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# 6. PCA for visualization
pca = PCA(n_components=2, random_state=42)
pca_result = pca.fit_transform(X_scaled)
df["PCA1"] = pca_result[:, 0]
df["PCA2"] = pca_result[:, 1]

# 7. Save result
df.to_csv("../data/customer_segments.csv", index=False)

# 8. Display result
print(df[["CustomerID", "Cluster"]].head(20))

# 9. PCA plot
plt.figure(figsize=(8, 6))
for cluster in sorted(df["Cluster"].unique()):
    part = df[df["Cluster"] == cluster]
    plt.scatter(part["PCA1"], part["PCA2"], label=f"Cluster {cluster}", alpha=0.65)

plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.title("Customer Segmentation using K-Means")
plt.legend()
plt.tight_layout()
plt.show()
