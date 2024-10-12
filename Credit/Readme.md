

# Credit Card Fraud Detection

## Overview

This project tackles the challenge of detecting fraudulent transactions in a highly imbalanced credit card dataset. The dataset contains 284,807 transactions, of which only 492 are fraudulent (0.17%).

## Dataset

- **Source**: [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Columns**: 31, including time of transaction, 28 anonymized features (`V1`, `V2`, ..., `V28`), `Amount`, and the target variable `Class` (0 = valid, 1 = fraudulent).
- **Shape**: `(284,807, 31)`

## Methodology

### Data Preprocessing

1. **Handling Imbalance**: Synthetic Minority Over-sampling Technique (SMOTE) was applied to balance the dataset.
2. **Feature Scaling**: Standard scaling was applied to `Amount` and `Time`.
3. **Train/Test Split**: 80/20 split with stratification to maintain the class distribution.

### Model Selection

We used **XGBoost**, a powerful gradient-boosting model, for its efficiency and performance in handling imbalanced datasets. RandomizedSearchCV was employed for hyperparameter tuning, with the following optimal parameters:

```python
{'scale_pos_weight': 577.876, 'reg_lambda': 0.1, 'reg_alpha': 0.01, 'n_estimators': 200, 'max_depth': 4, 'learning_rate': 0.1}
```

## Performance Metrics

### On Training Data:
- **Mean ROC-AUC (cross-validated)**: `0.999865`
- **Precision**: `1.00`
- **Recall**: `1.00`
- **F1-score**: `1.00`

### On Unseen Data:
- **ROC-AUC Score**: `0.991855`
- **Precision**: `1.00`
- **Recall**: `0.56`
- **F1-score**: `0.72`
  
The model performed extremely well, especially considering the small proportion of fraud cases. Fine-tuning and handling the extreme imbalance were key to this success.

## Conclusion

This project demonstrates the effectiveness of **XGBoost** with SMOTE in detecting fraud in highly imbalanced datasets. The model achieved near-perfect performance on training data and significant results on unseen data, indicating robustness and reliability.


