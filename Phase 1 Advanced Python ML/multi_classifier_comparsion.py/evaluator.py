import time
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_models(models, X_train, X_test, y_train, y_test, experiment_name="Multiclassifier_experiment"):
    mlflow.set_experiment(experiment_name)
    results = []

    for name, model in models.items():
        # Start a **new run for each model**
        with mlflow.start_run(run_name=name):
            start_time = time.time()
            model.fit(X_train, y_train)
            end_time = time.time()

            preds = model.predict(X_test)

            acc = accuracy_score(y_test, preds)
            prec = precision_score(y_test, preds, average="weighted")
            rec = recall_score(y_test, preds, average="weighted")
            f1 = f1_score(y_test, preds, average="weighted")
            training_time = end_time - start_time

            # Log parameters & metrics
            mlflow.log_param("model_type", name)
            if hasattr(model, "get_params"):
                mlflow.log_params(model.get_params())
            
            mlflow.log_metric("accuracy", acc)
            mlflow.log_metric("precision", prec)
            mlflow.log_metric("recall", rec)
            mlflow.log_metric("f1_score", f1)
            mlflow.log_metric("training_time", training_time)

            # Log the model itself
            mlflow.sklearn.log_model(model, artifact_path=name)

            results.append({
                "Model": name,
                "Accuracy": acc,
                "Precision": prec,
                "Recall": rec,
                "F1_Score": f1,
                "Training Time": training_time
            })

    return pd.DataFrame(results)
