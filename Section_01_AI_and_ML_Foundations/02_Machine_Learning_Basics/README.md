# Machine Learning Basics

## What is Machine Learning?

Machine Learning (ML) is a subset of AI that gives systems the ability to automatically learn and improve from experience without being explicitly programmed. Instead of writing rules, you provide data and let the algorithm discover patterns.

## The ML Paradigm Shift

**Traditional Programming:**
```
Data + Rules → Program → Output
```

**Machine Learning:**
```
Data + Output → ML Algorithm → Rules (Model)
```

## Core Concepts

### 1. Training Data
The dataset used to teach the model. Quality and quantity of training data directly impact model performance.

### 2. Features and Labels
- **Features (X)**: Input variables the model uses to make predictions
- **Labels (y)**: The target variable the model is trying to predict (in supervised learning)

### 3. Model
A mathematical function that maps inputs to outputs, learned from training data.

### 4. Training Process
1. Initialize model with random parameters
2. Feed training data through the model
3. Calculate the error (loss) between predictions and actual values
4. Adjust parameters to reduce error (optimization)
5. Repeat until error is minimized

### 5. Loss Function
Measures how far the model's predictions are from the actual values:
- **MSE (Mean Squared Error)** — for regression
- **Cross-Entropy Loss** — for classification
- **Hinge Loss** — for SVMs

### 6. Optimization
Algorithms that adjust model parameters to minimize loss:
- **Gradient Descent** — follow the slope of the loss function downhill
- **Stochastic Gradient Descent (SGD)** — use random subsets for speed
- **Adam** — adaptive learning rates (most popular today)

## The Three Pillars of ML

| Paradigm | Training Data | Goal | Example |
|----------|--------------|------|---------|
| **Supervised Learning** | Labeled (input-output pairs) | Predict outputs for new inputs | Email spam detection |
| **Unsupervised Learning** | Unlabeled (inputs only) | Discover hidden patterns | Customer segmentation |
| **Reinforcement Learning** | Rewards/penalties | Learn optimal behavior | Game-playing agents |

## Bias-Variance Tradeoff

One of the most fundamental concepts in ML:

- **Bias**: Error from overly simplistic assumptions (underfitting)
- **Variance**: Error from sensitivity to training data fluctuations (overfitting)
- **Goal**: Find the sweet spot that minimizes total error

```
High Bias + Low Variance = Underfitting (too simple)
Low Bias + High Variance = Overfitting (too complex)
Balanced = Good generalization
```

## Overfitting vs Underfitting

### Overfitting
- Model memorizes training data instead of learning general patterns
- Performs great on training data, poorly on new data
- **Solutions**: More data, regularization, dropout, early stopping, cross-validation

### Underfitting
- Model is too simple to capture patterns
- Performs poorly on both training and test data
- **Solutions**: More complex model, more features, less regularization, longer training

## Model Evaluation

### Train-Test Split
- Split data into training set (70-80%) and test set (20-30%)
- Train on training set, evaluate on test set
- Never use test data for training!

### Cross-Validation
- K-Fold: Split into K parts, train on K-1, test on 1, rotate
- Provides more robust performance estimates
- Standard: 5-fold or 10-fold cross-validation

### Key Metrics
- **Accuracy**: Correct predictions / Total predictions
- **Precision**: True Positives / (True Positives + False Positives)
- **Recall**: True Positives / (True Positives + False Negatives)
- **F1 Score**: Harmonic mean of Precision and Recall
- **AUC-ROC**: Area under the Receiver Operating Characteristic curve

## The ML Pipeline

```
Data Collection → Data Cleaning → Feature Engineering → 
Model Selection → Training → Evaluation → 
Hyperparameter Tuning → Deployment → Monitoring
```

## Connection to Agentic AI

- ML models form the **"brain"** of AI agents
- Agents use ML for **perception** (understanding inputs), **prediction** (anticipating outcomes), and **learning** (improving over time)
- Reinforcement Learning is the direct ancestor of agent-based decision making
- Understanding ML basics helps you choose the right models for different agent tasks
