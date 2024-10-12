# Disease Prediction: Breast Cancer and Stroke

This repository contains models developed for predicting breast cancer and stroke using machine learning techniques. The datasets used are the Breast Cancer dataset and Stroke Prediction dataset, sourced from Kaggle.

## Project Overview:
- **Breast Cancer Prediction Model**:
   - Dataset: [Breast Cancer Dataset](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset)
   - Optimized Accuracy: **0.982**
   - **Classification Report**:
     - **Precision**: 0.99 (for class 0), 0.98 (for class 1)
     - **Recall**: 0.99 (for class 0), 0.98 (for class 1)
     - **F1-Score**: 0.99 (for class 0), 0.98 (for class 1)
     - **Overall Accuracy**: 0.98

- **Stroke Prediction Model**:
   - Dataset: [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
   - Optimized Accuracy: **0.939**
   - **Classification Report**:
     - **Precision**: 0.94 (for class 0), 0.00 (for class 1)
     - **Recall**: 1.00 (for class 0), 0.00 (for class 1)
     - **F1-Score**: 0.97 (for class 0), 0.00 (for class 1)
     - **Overall Accuracy**: 0.94

### Weighted Stroke Model:
   - Weighted Accuracy: **0.750**
   - **Classification Report**:
     - **Precision**: 0.98 (for class 0), 0.17 (for class 1)
     - **Recall**: 0.75 (for class 0), 0.79 (for class 1)
     - **F1-Score**: 0.85 (for class 0), 0.28 (for class 1)
     - **Overall Accuracy**: 0.75

### SMOTE Stroke Model:
   - SMOTE Accuracy: **0.783**
   - **Classification Report**:
     - **Precision**: 0.98 (for class 0), 0.17 (for class 1)
     - **Recall**: 0.79 (for class 0), 0.69 (for class 1)
     - **F1-Score**: 0.87 (for class 0), 0.28 (for class 1)
     - **Overall Accuracy**: 0.78

Both models have been optimized and evaluated on their respective datasets, yielding robust results for breast cancer detection and a variety of results using different techniques for stroke prediction, including weighted and SMOTE adjustments.
