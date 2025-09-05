from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def train_logistic_regression(X_train, y_train):
    """Trains a Logistic Regression model."""
    lr_model = LogisticRegression(max_iter=500)
    lr_model.fit(X_train, y_train)
    return lr_model

def train_random_forest(X_train, y_train):
    """Trains a Random Forest Classifier."""
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train, y_train)
    return rf_model

def train_svc(X_train, y_train):
    """Trains a Support Vector Machine Classifier."""
    svc_model = SVC(probability=True, random_state=42)
    svc_model.fit(X_train, y_train)
    return svc_model