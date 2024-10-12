# Health Prediction Models: Breast Cancer and Stroke Prediction

## Overview

This repository contains two machine learning models designed for healthcare-related predictions:

- **Breast Cancer Prediction Model**
- **Stroke Prediction Model**

Both models use public datasets to predict outcomes related to breast cancer diagnosis and stroke occurrence, employing several machine learning techniques, optimizations, and evaluations.

---

## Datasets

1. **[Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)**
   - This dataset contains patient information and their stroke history, including features such as age, gender, hypertension, heart disease, average glucose level, BMI, and more. The target variable is whether the patient has had a stroke.

2. **[Breast Cancer Dataset](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset)**
   - This dataset consists of various measurements derived from breast cancer tumor features. The target variable indicates whether the tumor is benign or malignant.

---

## Key Results

### 1. **Breast Cancer Prediction Model**

- **Best Model**: Logistic Regression (after feature scaling and tuning)
- **Accuracy**: `98.25%`
- **Classification Report**:

   | Precision | Recall | F1-Score | Support |
   |-----------|--------|----------|---------|
   | 0 (Benign) | 0.99 | 0.99 | 0.99 | 71 |
   | 1 (Malignant) | 0.98 | 0.98 | 0.98 | 43 |
   | **Overall Accuracy** | | | **0.98** | **114** |

- **Observations**:
   - The model performs exceptionally well on both benign and malignant cases, with high precision and recall for both classes.
   - The f1-score is balanced, which indicates the model is neither overfitting nor underfitting.

### 2. **Stroke Prediction Model**

- **Best Model**: Logistic Regression
- **Accuracy**: `93.93%`
- **Classification Report**:

   | Precision | Recall | F1-Score | Support |
   |-----------|--------|----------|---------|
   | 0 (No Stroke) | 0.94 | 1.00 | 0.97 | 960 |
   | 1 (Stroke) | 0.00 | 0.00 | 0.00 | 62 |
   | **Overall Accuracy** | | | **0.94** | **1022** |

- **Challenges**:
   - The model performs very well for classifying non-stroke cases but struggles with identifying stroke cases (class imbalance).
   - Applying oversampling methods (e.g., SMOTE) improves the recall and f1-score for the minority class, but challenges remain with precision and overall accuracy.
   
---


## Stroke Model Enhancements

### SMOTE (Synthetic Minority Over-sampling Technique)

To address the class imbalance in the stroke dataset, SMOTE was applied. The following are results after applying SMOTE:

- **Accuracy**: `93.11%`
- **Classification Report** (with SMOTE):

   | Precision | Recall | F1-Score | Support |
   |-----------|--------|----------|---------|
   | 0 (No Stroke) | 0.98 | 0.88 | 0.93 | 975 |
   | 1 (Stroke) | 0.89 | 0.98 | 0.93 | 970 |

   **Overall Accuracy**: `0.93` with `1945` total samples.
   
   **Macro Avg**: Precision: `0.94`, Recall: `0.93`, F1-Score: `0.93`  
   **Weighted Avg**: Precision: `0.94`, Recall: `0.93`, F1-Score: `0.93`

- **Observations**:
   - SMOTE drastically improved the model's performance in predicting stroke cases (`Recall: 0.98`).
   - The overall balance between precision, recall, and f1-score indicates that the model can now correctly identify both stroke and non-stroke cases effectively.

--- 



## Limitations and Future Work

1. **Breast Cancer Model**:
   - The breast cancer dataset is relatively balanced, so model performance is consistently high across classes. However, exploring deeper models like neural networks could further improve results.

2. **Stroke Model**:
   - The stroke prediction task faces significant challenges due to the class imbalance.
   - The model's precision for detecting stroke remains low even after SMOTE. Future work should explore advanced ensemble methods, anomaly detection techniques, and alternative feature engineering strategies.
   
---

## Model Warnings and Issues

1. **Convergence Warning**: 
   - During training, the logistic regression models (both stroke and breast cancer) occasionally raised convergence warnings, indicating that the algorithm had reached the maximum number of iterations without converging.
   - These warnings were mitigated by increasing the `max_iter` parameter but did not significantly affect the model's final accuracy.

2. **Undefined Metric Warning**:
   - For the stroke prediction model, precision and f1-score were reported as `0.0` for the minority class due to the lack of predicted samples. This was mainly observed in the non-SMOTE models.

---

This README provides an overview of the performance, results, and challenges in the breast cancer and stroke prediction models in this repository. Further model improvements can be achieved through handling class imbalance in the stroke dataset and experimenting with more advanced machine learning algorithms.


