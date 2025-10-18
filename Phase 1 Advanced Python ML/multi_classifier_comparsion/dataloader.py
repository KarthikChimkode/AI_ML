from sklearn.datasets import load_iris, load_wine
from sklearn.model_selection import train_test_split

def load_data(dataset_name="iris", test_size=0.2, random_state=42):
    if dataset_name == "iris":
        data = load_iris()
    elif dataset_name == "wine":
        data = load_wine()
    else:
        raise ValueError("Dataset not supported. Use 'iris' or 'wine'.")
    

    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return X_train, X_test, y_train, y_test, data.feature_names, data.target_names