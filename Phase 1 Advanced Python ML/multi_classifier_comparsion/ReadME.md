```markdown
# Multi-Classifier Comparison (Decision Tree, Random Forest, Logistic Regression)

This project demonstrates the comparison of multiple machine learning classifiers on a standard dataset (Iris or Wine) using Python, scikit-learn, and MLflow. It evaluates model performance based on accuracy, precision, recall, F1-score, and training time, with visualizations for easy comparison.

```

## 📂 Project Structure

```
multi_classifier_comparison/
│
├── main.py                # Entry point: loads dataset, trains models, calls evaluation and plotting
├── evaluator.py           # Contains evaluate_models function with MLflow logging
├── plotter.py             # Functions for plotting metrics and training times
├── data/                  # Folder for datasets (Iris, Wine)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

````

---

## 🛠️ Installation

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd multi_classifier_comparison
````

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv mlprojects
source mlprojects/Scripts/activate  # Windows
# or
source mlprojects/bin/activate      # macOS/Linux
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

> Make sure you have Python 3.9+ and pip updated.

---

## 🚀 Usage

1. **Run the main script**

```bash
python main.py
```

This will:

* Load the dataset (Iris by default)
* Train Decision Tree, Random Forest, and Logistic Regression classifiers
* Evaluate each model using test data
* Log metrics and models in MLflow
* Plot comparison charts for metrics and training time

2. **View MLflow UI**

```bash
mlflow ui
```

* Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)
* View each model run, parameters, metrics, and logged models

---

## 🧮 Features

* Multi-class classifier evaluation
* Performance metrics: Accuracy, Precision, Recall, F1-Score
* Training time comparison
* Cross-validation ready for robust scores
* MLflow integration for logging and experiment tracking
* Matplotlib visualizations for quick comparisons

---

## 📊 Visualizations

1. **Performance Metrics Bar Chart**

   * Compares Accuracy, Precision, Recall, and F1-Score across all models

2. **Training Time Bar Chart**

   * Compares the training duration of each model

---

## 🧩 Extending the Project

* Add more classifiers (SVM, KNN, Gradient Boosting)
* Add more datasets (Wine, Breast Cancer, custom CSV files)
* Include cross-validation metrics in plots
* Save plots as images or HTML reports

---

## 📄 References

* [Scikit-learn Documentation](https://scikit-learn.org/stable/)
* [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
* [Matplotlib Documentation](https://matplotlib.org/stable/index.html)

---

## 👤 Author

Karthik Chimkode 

---
