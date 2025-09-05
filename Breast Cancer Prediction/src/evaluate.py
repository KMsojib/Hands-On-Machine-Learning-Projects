from sklearn.metrics import classification_report, accuracy_score

def evaluate_model(model, X_test, y_test):
    """Prints a classification report and accuracy score for a given model."""
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    return accuracy_score(y_test, y_pred)