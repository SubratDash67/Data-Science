# Machine Learning Models Repository
 This repository hosts a collection of diverse projects, each targeting a unique domain, from financial fraud detection and customer segmentation to healthcare predictions. Each project demonstrates the end-to-end process of building, tuning, and evaluating models, from data preprocessing to interpreting results. Below is an overview of the models and methodologies employed in this repository:

---

## 1. **Credit Card Fraud Detection**

### Objective

The goal of this project is to detect fraudulent credit card transactions from a highly imbalanced dataset, where only 0.17% of transactions are fraudulent. By leveraging advanced machine learning techniques and oversampling methods, this project seeks to create a robust, accurate fraud detection model.

### Dataset Overview

- **Source**: [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Transactions**: 284,807
- **Fraudulent transactions**: 492 (0.17%)
- **Features**: 30 anonymized transaction features + `Amount`, `Time`, and `Class` (target variable).

### Key Techniques

- **Imbalance Handling**: **SMOTE** (Synthetic Minority Over-sampling Technique) was used to address the extreme class imbalance.
- **Feature Scaling**: Standardization applied to `Amount` and `Time` to align them with the anonymized features.
- **Model**: **XGBoost**, a gradient-boosting model known for handling imbalanced data efficiently.
- **Hyperparameter Tuning**: Employed **RandomizedSearchCV** to find the optimal set of parameters.

### Results

- **Training ROC-AUC**: `0.999865`
- **Test ROC-AUC**: `0.991855`
- **Precision**: `1.00`
- **Recall**: `0.56`
- **F1-Score**: `0.72`

### Conclusion

The model achieved near-perfect performance on the training data and impressive results on unseen data, highlighting the success of **XGBoost** in fraud detection. While the recall on test data is relatively lower, precision remained high, indicating that fraudulent transactions identified by the model are accurate.

---

## 2. **Customer Segmentation Using Online Retail Dataset**

### Objective

This project focuses on **customer segmentation** based on their purchasing behavior. By identifying distinct customer segments, businesses can tailor their marketing strategies, leading to better customer retention and increased sales.

### Dataset Overview

- **Source**: [Online Retail Dataset](https://www.kaggle.com/datasets/divanshu22/online-retail-dataset)
- **Records**: 541,909 transactions
- **Features**: 8 columns including `InvoiceNo`, `StockCode`, `Quantity`, `UnitPrice`, `CustomerID`, `Country`, etc.

### Key Techniques

- **Data Cleaning**: Handled missing values for `CustomerID`, treated negative values in `Quantity` and `UnitPrice` as product returns or adjustments.
- **Feature Engineering**: Created `TotalAmount` (Quantity * UnitPrice) to better capture purchase behavior.
- **Segmentation Approach**: Applied **RFM Analysis** (Recency, Frequency, Monetary) to categorize customers based on their purchase behavior.
- **Clustering Model**: **K-Means** clustering was used to group customers into distinct segments based on RFM values.

### Results

- **Segment 1**: High-frequency customers with high monetary value, representing loyal customers.
- **Segment 2**: Customers with high recency but lower monetary engagement, potential targets for reactivation campaigns.
- **Segment 3**: Low-frequency, low-monetary customers, likely occasional or one-time buyers.

### Conclusion

The clustering approach effectively identified three distinct customer segments. These insights provide a foundation for personalized marketing strategies, allowing businesses to allocate resources efficiently based on customer behavior.

---

## 3. **Health Prediction Models: Breast Cancer and Stroke Prediction**

### Objective

This section of the repository features two healthcare prediction models aimed at predicting outcomes related to breast cancer diagnosis and stroke occurrences. These models demonstrate the application of machine learning in healthcare, helping improve early diagnosis and prevention strategies.

### 3.1 **Breast Cancer Prediction**

#### Dataset Overview

- **Source**: [Breast Cancer Dataset](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset)
- **Target**: Binary classification of tumors as **benign** or **malignant**.
- **Features**: Several measurements derived from tumor features.

#### Key Techniques

- **Model**: **Logistic Regression**, chosen for its interpretability and performance on smaller datasets.
- **Feature Scaling**: Applied standard scaling to features for consistent model training.

#### Results

- **Accuracy**: `98.25%`
- **Precision (Benign)**: `0.99`
- **Precision (Malignant)**: `0.98`
- **Recall (Malignant)**: `0.98`

#### Conclusion

The model demonstrated high accuracy, precision, and recall, making it a robust tool for predicting breast cancer outcomes. The model balanced both benign and malignant classifications effectively, with minimal overfitting.

### 3.2 **Stroke Prediction**

#### Dataset Overview

- **Source**: [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
- **Target**: Predict whether a patient is likely to have a stroke.
- **Features**: Patient details including age, gender, hypertension, heart disease, average glucose levels, BMI, etc.

#### Key Techniques

- **Model**: **Logistic Regression**, due to its simplicity and suitability for binary classification.
- **Class Imbalance Handling**: Applied **SMOTE** to balance the distribution of stroke and non-stroke cases.

#### Results

- **Accuracy**: `93.93%` (without SMOTE), improved to `93.11%` (with SMOTE).
- **Recall (Stroke)**: Improved from `0.00` to `0.98` after applying SMOTE.

#### Conclusion

Handling class imbalance was a critical step in improving the performance of the stroke prediction model. While the initial model struggled with identifying stroke cases, SMOTE dramatically increased the model’s ability to correctly predict stroke occurrences, making it a more reliable predictive tool.

---

## Key Technologies Used

- **Python**: Primary programming language for all projects.
- **Pandas**: For data manipulation and cleaning.
- **scikit-learn**: Core library used for model building, feature scaling, and evaluation.
- **XGBoost**: Applied for credit card fraud detection, known for its performance in imbalanced datasets.
- **K-Means Clustering**: Used for customer segmentation to identify meaningful customer groups.
- **SMOTE**: Synthetic oversampling technique to handle imbalanced datasets, applied in the stroke and fraud detection models.

---

## Future Improvements

- **Advanced Models**: While traditional models like Logistic Regression and XGBoost performed well, future work could explore deeper models such as **Neural Networks** or **Ensemble Methods** for further improvements.
- **Anomaly Detection**: For fraud and stroke prediction, anomaly detection algorithms could be considered to enhance precision for rare events.
- **Feature Engineering**: More sophisticated feature engineering, particularly in customer segmentation and healthcare models, could reveal additional patterns and insights.

---

## Conclusion

This repository showcases how machine learning models can be applied across various domains to solve real-world problems effectively. The careful use of techniques such as oversampling, feature scaling, and hyperparameter tuning has helped these models achieve competitive results. These projects serve as foundational examples for both beginners and experts looking to explore machine learning solutions in finance, retail, and healthcare.

---

Feel free to clone this repository and explore the code and datasets used in each project. Contributions and feedback are always welcome!
