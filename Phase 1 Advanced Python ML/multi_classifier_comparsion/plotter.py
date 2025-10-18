import matplotlib.pyplot as plt
import numpy as np

def plot_metrics(df):
    import matplotlib.pyplot as plt
    import numpy as np

    metrics = ["Accuracy", "Precision", "Recall", "F1_Score"]  # keep original column names
    n_metrics = len(metrics)
    n_models = len(df)

    x = np.arange(n_metrics)
    width = 0.2

    for i, row in enumerate(df.itertuples(index=False)):
        row_dict = row._asdict()  # convert namedtuple to dict
        values = [row_dict[m] for m in metrics]  # access by column name safely
        plt.bar(x + i*width, values, width, label=row_dict["Model"])

    plt.xticks(x + width*(n_models-1)/2, metrics)
    plt.ylabel("Score")
    plt.title("Model Comparison")
    plt.ylim(0, 1.1)
    plt.legend()
    plt.show()



def plot_training_time(results_df):
    plt.figure(figsize=(8,5))
    plt.bar(results_df["Model"], results_df["Training Time"], color='orange')
    plt.ylabel("Training Time (s)")
    plt.title("Training Time Comparison")
    plt.show()
        