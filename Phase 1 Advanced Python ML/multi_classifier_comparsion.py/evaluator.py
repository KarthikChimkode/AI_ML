import time 
import pandas as pd 
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import cross_val_score

def evaluate_models(models, X_train, X_test, y_train, y_test, X, y):
    results = []

    for name, model in models.items():
        start = time.time()
        model.fit(X_train, y_train)
        train_time = time.time() - start

        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average='weighted')
        rec = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')
        cv_acc = cross_val_score(model, X, y, cv=5, scoring='accuracy').mean()

        results.append({
            "Model":name,
            "Accuracy":prec,
            "Precission":rec,
            "F1-Score":f1,
            "CV Accuracy": cv_acc,
            "Training Times (s)":train_time
        })

    results_df = pd.DataFrame(results)
    return results_df
