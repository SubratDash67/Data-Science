

# Customer Segmentation - Online Retail Dataset

This repository contains the project for **Customer Segmentation** using the [Online Retail Dataset](https://www.kaggle.com/datasets/divanshu22/online-retail-dataset) from Kaggle. The goal is to segment customers into distinct groups based on their purchasing behavior, which can help businesses tailor marketing strategies and improve customer retention.

## Dataset Overview

The dataset contains transactional data for an online retail store based in the UK between 2010 and 2011. It includes information about the product orders made by various customers across different countries.

### Key Columns

- **InvoiceNo**: Invoice number for the transaction.
- **StockCode**: Product code for the purchased item.
- **Description**: Description of the product.
- **Quantity**: Number of items purchased in the transaction.
- **InvoiceDate**: Date and time of the transaction.
- **UnitPrice**: Price of each product.
- **CustomerID**: Unique identifier for each customer.
- **Country**: The country where the customer is located.

### Data Characteristics

- **Number of rows**: 541,909
- **Number of columns**: 8

### Key Insights

- The dataset contains **missing values** for `CustomerID` in approximately 25% of the records.
- **Negative values** are present in both the `Quantity` and `UnitPrice` columns, typically indicating product returns or adjustments.
- The majority of the transactions are made by customers from the **United Kingdom**.

## Project Workflow

1. **Data Cleaning**:
   - Handle missing values (e.g., removing rows with missing `CustomerID`).
   - Remove or treat records with negative `Quantity` and `UnitPrice` values.
   - Feature engineering to create meaningful variables (e.g., `TotalAmount = Quantity * UnitPrice`).
   
2. **Exploratory Data Analysis (EDA)**:
   - Distribution of purchases across different countries.
   - Analysis of customer purchasing patterns.
   - Identification of outliers in `Quantity` and `UnitPrice`.

3. **Customer Segmentation**:
   - **RFM Analysis**: 
     - Recency: Days since the customer's last purchase.
     - Frequency: Total number of purchases made by the customer.
     - Monetary: Total amount spent by the customer.
   - **K-Means Clustering**:
     - Group customers based on the RFM features to identify distinct segments.
   
4. **Model Evaluation**:
   - Visualize the clustering results.
   - Evaluate the coherence of customer groups using metrics like silhouette scores.

## Technologies Used

- **Python**: Main programming language.
- **Pandas**: Data manipulation and analysis.
- **Matplotlib / Seaborn**: Data visualization.
- **scikit-learn**: For K-means clustering and model evaluation.
  


## Results

- **Segment 1**: High-frequency customers with high monetary value, typically long-time loyal customers.
- **Segment 2**: Customers with high recency but lower spending.
- **Segment 3**: Low-frequency, low-monetary customers who might be one-time buyers or have low engagement.
  
The clustering results can be used to target each customer segment with personalized marketing strategies.

## Conclusion

This project demonstrates the application of clustering techniques to segment customers based on purchasing behavior, providing valuable insights for businesses to improve customer retention and targeting.

