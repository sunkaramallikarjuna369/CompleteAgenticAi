# Classical ML Algorithms

## Overview

Classical ML algorithms remain the backbone of many production systems, especially for structured/tabular data. Understanding these algorithms provides the foundation for appreciating why deep learning and neural networks were needed for more complex tasks.

## Decision Trees

**How it works:** Splits data recursively based on feature values to create a tree-like structure of decisions.

**Key Concepts:**
- **Splitting Criteria:** Information Gain (Entropy), Gini Impurity
- **Pruning:** Removing branches to prevent overfitting
- **Depth:** Controls complexity — deeper = more complex

**Strengths:** Interpretable, handles mixed data types, no feature scaling needed
**Weaknesses:** Prone to overfitting, unstable (small data changes → different trees)

## Random Forest

**How it works:** Ensemble of many decision trees, each trained on a random subset of data and features. Final prediction is the majority vote (classification) or average (regression).

**Key Concepts:**
- **Bagging:** Bootstrap Aggregation — train each tree on a random sample with replacement
- **Feature Randomness:** Each split considers only a random subset of features
- **Out-of-Bag (OOB) Score:** Built-in validation using samples not used in each tree

**Strengths:** Robust, handles overfitting, feature importance ranking
**Weaknesses:** Less interpretable than single tree, slower for large datasets

## Gradient Boosting (XGBoost, LightGBM, CatBoost)

**How it works:** Builds trees sequentially, where each new tree corrects the errors of all previous trees combined.

**Key Concepts:**
- **Boosting:** Sequential ensemble — each model focuses on previous errors
- **Learning Rate:** Controls contribution of each tree (shrinkage)
- **Regularization:** L1/L2 penalties to prevent overfitting

**XGBoost:** The gold standard for tabular data competitions. Optimized gradient boosting with regularization.
**LightGBM:** Faster than XGBoost using histogram-based splitting and leaf-wise growth.
**CatBoost:** Handles categorical features natively without encoding.

## Support Vector Machines (SVM)

**How it works:** Finds the hyperplane that maximally separates classes with the widest margin.

**Key Concepts:**
- **Margin:** Distance between decision boundary and nearest points
- **Support Vectors:** The critical points closest to the boundary
- **Kernel Trick:** Maps data to higher dimensions for non-linear boundaries (RBF, Polynomial)

**Strengths:** Effective in high dimensions, memory efficient (only stores support vectors)
**Weaknesses:** Slow on large datasets, sensitive to feature scaling

## K-Nearest Neighbors (KNN)

**How it works:** Classifies a point based on the majority class of its K nearest neighbors. No training phase — all computation happens at prediction time.

**Strengths:** Simple, no training, works well for small datasets
**Weaknesses:** Slow prediction (must search all data), curse of dimensionality

## Naive Bayes

**How it works:** Applies Bayes' theorem with the "naive" assumption that features are independent.

**Variants:** Gaussian (continuous), Multinomial (counts), Bernoulli (binary)
**Strengths:** Very fast, works well with high-dimensional data, great for text classification
**Weaknesses:** Independence assumption rarely holds in practice

## Linear and Logistic Regression

**Linear Regression:** Fits a line/hyperplane to predict continuous values. Foundation of ML.
**Logistic Regression:** Uses sigmoid function for binary classification. Despite name, it's a classifier.
**Regularized variants:** Ridge (L2), Lasso (L1), Elastic Net (L1+L2)

## Algorithm Selection Guide

| Scenario | Recommended Algorithm |
|----------|----------------------|
| Small dataset, need interpretability | Decision Tree |
| Tabular data, best accuracy needed | XGBoost / LightGBM |
| High-dimensional data | SVM with RBF kernel |
| Text classification, fast training | Naive Bayes |
| Need feature importance | Random Forest |
| Simple baseline | Logistic/Linear Regression |
| Small dataset, lazy evaluation | KNN |

## Connection to Agentic AI

- These algorithms are used as **sub-components** in agent systems (classification, routing, scoring)
- **Gradient Boosting** models often serve as lightweight classifiers within agent pipelines
- Understanding classical ML helps you choose when to use a simple model vs a complex LLM-based approach
- **Feature engineering** concepts from classical ML inform how we design agent inputs and prompts
