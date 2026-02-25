# Supervised Learning

## Overview

Supervised Learning is the most common ML paradigm. The algorithm learns from labeled training data — input-output pairs — to make predictions on new, unseen data. Think of it as learning with a teacher who provides the correct answers.

## How It Works

```
Training Phase:
  Input Features (X) + Known Labels (y) → Algorithm → Trained Model

Prediction Phase:
  New Input Features (X_new) → Trained Model → Predicted Labels (y_pred)
```

## Two Main Types

### 1. Classification
Predicting discrete categories or classes.

**Binary Classification** — Two classes (Yes/No, Spam/Not Spam, Positive/Negative)
**Multi-class Classification** — Multiple classes (Cat/Dog/Bird, Sentiment: Positive/Neutral/Negative)
**Multi-label Classification** — Multiple labels per instance (a movie can be Action AND Comedy)

**Key Algorithms:**
- Logistic Regression
- Decision Trees
- Random Forest
- Support Vector Machines (SVM)
- K-Nearest Neighbors (KNN)
- Naive Bayes
- Neural Networks

### 2. Regression
Predicting continuous numerical values.

**Examples:** House prices, temperature, stock prices, sales forecasting

**Key Algorithms:**
- Linear Regression
- Polynomial Regression
- Ridge/Lasso Regression
- Decision Tree Regression
- Random Forest Regression
- Gradient Boosting (XGBoost, LightGBM)
- Neural Networks

## Key Algorithms Explained

### Logistic Regression
Despite its name, used for classification. Applies a sigmoid function to linear regression output to produce probabilities between 0 and 1.

### Decision Trees
Tree-structured model that makes decisions by splitting data based on feature values. Easy to interpret but prone to overfitting.

### Random Forest
Ensemble of many decision trees. Each tree trained on a random subset of data and features. Reduces overfitting through averaging.

### Support Vector Machines (SVM)
Finds the optimal hyperplane that maximally separates classes. Effective in high-dimensional spaces. Can use kernel trick for non-linear boundaries.

### Gradient Boosting (XGBoost, LightGBM, CatBoost)
Builds trees sequentially, each correcting errors of the previous. Currently among the best performing algorithms for structured/tabular data.

## Evaluation Metrics

### For Classification
| Metric | What It Measures | When to Use |
|--------|-----------------|-------------|
| **Accuracy** | Overall correctness | Balanced classes |
| **Precision** | Exactness of positive predictions | Cost of false positives is high |
| **Recall** | Completeness of positive predictions | Cost of false negatives is high |
| **F1 Score** | Balance of precision and recall | Imbalanced classes |
| **AUC-ROC** | Ranking quality | Need probability outputs |
| **Confusion Matrix** | Detailed error breakdown | Understanding error types |

### For Regression
| Metric | What It Measures |
|--------|-----------------|
| **MSE** | Average squared error |
| **RMSE** | Root of MSE (same units as target) |
| **MAE** | Average absolute error |
| **R² Score** | Proportion of variance explained |
| **MAPE** | Percentage error |

## Practical Considerations

1. **Data Quality** — Garbage in, garbage out. Clean, relevant data is essential
2. **Feature Selection** — Choose the most informative features
3. **Class Imbalance** — When one class dominates, use SMOTE, class weights, or resampling
4. **Regularization** — L1 (Lasso) for feature selection, L2 (Ridge) for preventing large weights
5. **Cross-Validation** — Always validate to get robust performance estimates
6. **Hyperparameter Tuning** — Use Grid Search or Random Search or Bayesian Optimization

## Connection to Agentic AI

- Supervised learning powers many agent sub-components: intent classification, entity extraction, sentiment analysis
- Agent evaluation often uses supervised learning metrics (accuracy, F1) to assess agent quality
- Fine-tuning LLMs is essentially supervised learning on instruction-following data
- Understanding classification vs regression helps you design agent outputs appropriately
