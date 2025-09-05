# 🩺 Medical Diagnosis Prediction (Breast Cancer)

## 📖 Overview
This repository contains a machine learning project focused on **Breast Cancer Prediction**. The primary objective is to develop and evaluate models that can accurately classify tumors as either benign or malignant based on a set of features.

The project covers a complete machine learning workflow, including:
- **Data Exploration (EDA):** Initial analysis and understanding of the dataset.
- **Model Training & Comparison:** Building and evaluating three different models: Logistic Regression, Random Forest, and a Support Vector Machine (SVM).
- **Explainability (XAI):** Using cutting-edge techniques like SHAP and LIME to interpret model predictions.
- **Reporting:** Generating performance reports and visual figures to summarize the findings.

---

## 📊 Results Summary
The models were trained and evaluated on the scikit-learn breast cancer dataset. The table below summarizes the performance of each model.

| Dataset       | Best Model          | Other Models Used       | ROC-AUC | Recall | Precision | Notes                               |
|---------------|---------------------|-------------------------|---------|--------|-----------|-------------------------------------|
| Breast Cancer | **Logistic Regression** | **Random Forest**<br>**SVM** | 0.99    | 0.96   | 0.95      | Excellent performance with good interpretability. |

---

## 📂 Repository Structure

- **breast_cancer_prediction/**:
  - `data/`: Placeholder for raw and processed data.
  - `notebooks/`: Jupyter notebooks used for development.
    - `Check 3 code file `: where contain all codes, from data loading to model explainability.
  - `reports/`:
    - `figures/`: Contains generated plots, such as SHAP summary plots and LIME explanations.
  - `README.md`: This file, providing an overview of the project.

---
