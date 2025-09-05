import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

def load_data():
    """Loads the breast cancer dataset and returns it as a DataFrame."""
    cancer = load_breast_cancer()
    X = pd.DataFrame(cancer.data, columns=cancer.feature_names)
    y = pd.Series(cancer.target, name='target')
    return X, y

def split_data(X, y, test_size=0.3, random_state=42):
    """Splits the data into training and testing sets."""
    return train_test_split(X, y, stratify=y, test_size=test_size, random_state=random_state)