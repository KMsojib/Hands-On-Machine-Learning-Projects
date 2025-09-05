# 🩺 Medical Diagnosis ML — Breast Cancer Prediction

## 📖 Overview
This repository contains a machine learning project focused on **Breast Cancer Prediction**. The objective is to develop and evaluate models that classify tumors as benign or malignant based on key clinical features.

The workflow includes:
- **Data Exploration (EDA):** Understand feature distributions and correlations.
- **Model Training & Comparison:** Train and evaluate Logistic Regression, Random Forest, SVM, and Decision Tree models.
- **Explainability (XAI):** Interpret predictions using SHAP and LIME.
- **Reporting:** Generate performance metrics and visual figures for model evaluation.

---

## 📊 Model Performance Summary
The models were trained on the scikit-learn breast cancer dataset. The table below summarizes full-data accuracy and cross-validation performance.

| Model                              | Full-Data Accuracy | Cross-Validation Score (Average)    | Notes                                   |
|----------------------------------- |-----------------   |---------------------------------    |-----------------------------------------|
| Decision Tree Classifier           | 1.00               | 1.00                                | Perfect classification on full dataset. |
| Random Forest Classifier           | 1.00               | 0.994                               | High accuracy with ensemble robustness. |
| Logistic Regression                | 0.90               | 0.906                               | Strong baseline with interpretability.  |
| Support Vector Classifier (SVC)    | 0.89               | 0.886                               | Good performance, sensitive to scaling. |

> Note: Decision Tree and Random Forest achieved perfect accuracy on the full dataset, indicating strong classification capability.


## 📌 Key Highlights
- Built and compared multiple ML models for breast cancer prediction.
- Achieved ROC-AUC of 0.99 with Logistic Regression.
- Applied SHAP and LIME for model interpretability.
- Demonstrated robust performance with cross-validation and full-data accuracy checks.
- Provided a reproducible pipeline for healthcare ML tasks.
