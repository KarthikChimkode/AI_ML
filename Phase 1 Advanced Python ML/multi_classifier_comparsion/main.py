from dataloader import load_data
from models import get_models
from evaluator import evaluate_models
from plotter import plot_metrics, plot_training_time

def main():
    X_train, X_test, y_train, y_test, feature_names, target_names = load_data("iris")
    models = get_models()
    print(f"Loaded dataset with {len(target_names)} classes.")

    experiment_name = "iris_experiment"

    result_df = evaluate_models(models, X_train, X_test, y_train, y_test, experiment_name)
        
    print(result_df)

    plot_metrics(result_df)
    plot_training_time(result_df)

    best_model = result_df.loc[result_df["Accuracy"].idxmax()]
    print(f"\n Best Model: {best_model['Model']} with accuracy {best_model['Accuracy']:.3f}")

if __name__ == "__main__":
    main()