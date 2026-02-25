# Unsupervised Learning

## Overview

Unsupervised Learning discovers hidden patterns and structures in data without labeled examples. The algorithm must find meaningful organization in the data on its own.

## Key Techniques

### 1. Clustering
Grouping similar data points together.

**K-Means Clustering**
- Partition data into K clusters by minimizing within-cluster distance
- Simple, fast, scales well
- Must choose K in advance (use Elbow Method or Silhouette Score)

**DBSCAN (Density-Based Spatial Clustering)**
- Groups points in dense regions, marks sparse points as outliers
- No need to specify K
- Handles arbitrary cluster shapes

**Hierarchical Clustering**
- Builds a tree (dendrogram) of nested clusters
- Can be agglomerative (bottom-up) or divisive (top-down)
- Visual and interpretable

### 2. Dimensionality Reduction
Reducing the number of features while preserving important information.

**PCA (Principal Component Analysis)**
- Finds directions of maximum variance
- Projects data onto fewer dimensions
- Linear transformation

**t-SNE (t-distributed Stochastic Neighbor Embedding)**
- Non-linear dimensionality reduction
- Excellent for visualization in 2D/3D
- Preserves local structure

**UMAP (Uniform Manifold Approximation)**
- Faster than t-SNE, better global structure
- Good for both visualization and as a preprocessing step

### 3. Anomaly Detection
Identifying unusual data points that don't fit normal patterns.

**Isolation Forest** — Isolates anomalies by random partitioning
**One-Class SVM** — Learns boundary around normal data
**Autoencoders** — Neural networks that reconstruct normal data; anomalies have high reconstruction error

### 4. Association Rule Mining
Discovering relationships between variables (e.g., market basket analysis).

**Apriori Algorithm** — Finds frequent itemsets
**FP-Growth** — More efficient frequent pattern mining

## Applications

| Technique | Application | Example |
|-----------|------------|---------|
| Clustering | Customer Segmentation | Group customers by behavior for targeted marketing |
| Clustering | Document Grouping | Organize articles by topic |
| Dim. Reduction | Data Visualization | Visualize high-dimensional embeddings in 2D |
| Dim. Reduction | Feature Engineering | Reduce noise, speed up training |
| Anomaly Detection | Fraud Detection | Flag unusual transactions |
| Anomaly Detection | System Monitoring | Detect server anomalies |
| Association Rules | Recommendation | "Customers who bought X also bought Y" |

## Connection to Agentic AI

- **Vector embeddings** used by agents rely on dimensionality reduction concepts
- **Clustering** helps agents organize knowledge and group similar tasks
- **Anomaly detection** enables agents to identify unusual situations requiring special handling
- **Topic modeling** (an unsupervised technique) helps agents understand document collections
- RAG systems use embedding spaces where unsupervised learning concepts are fundamental
