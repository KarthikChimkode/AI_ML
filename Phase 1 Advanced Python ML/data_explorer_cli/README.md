
```markdown
# 🧮 Data Explorer CLI

A lightweight **Command-Line Interface (CLI)** tool for quickly exploring and analyzing CSV datasets — built entirely in **Python** using `argparse` and `pandas`.

This project is perfect for ML practitioners and data engineers who want a **fast, scriptable data summary tool**.

---

## 🚀 Features

✅ Load and summarize CSV datasets  
✅ View dataset shape and first few rows  
✅ Generate descriptive statistics (mean, std, min, max, etc.)  
✅ Check for missing values  
✅ Display correlation matrix between numeric columns  
✅ Combine multiple analysis flags in one command  

---

## 🧩 Project Structure

```

data_explorer_cli/
│
├── data_explorer.py         # Main entry point (CLI interface)
├── explorer/
│   ├── **init**.py
│   ├── cli.py               # Handles argument parsing and CLI logic
│   ├── loader.py            # Handles dataset loading
│   └── summary.py           # Handles data summarization and stats
│
└── data/
└── customers-100.csv    # Sample dataset

````

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/data-explorer-cli.git
   cd data-explorer-cli
````

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate     # For Linux/Mac
   venv\Scripts\activate        # For Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install pandas
   ```

---

## 🧠 Usage

You can run the CLI directly from the terminal:

```bash
python data_explorer.py --file data/customers-100.csv [options]
```

### 🔹 Available Options

| Option          | Description                                     |
| --------------- | ----------------------------------------------- |
| `--file <path>` | Path to your CSV file (required)                |
| `--head`        | Show first 5 rows of the dataset                |
| `--describe`    | Show descriptive statistics                     |
| `--missing`     | Show missing value counts                       |
| `--correlation` | Show correlation matrix between numeric columns |

---

## 🧪 Examples

**1️⃣ View first 5 rows**

```bash
python data_explorer.py --file data/customers-100.csv --head
```

**2️⃣ Get dataset summary**

```bash
python data_explorer.py --file data/customers-100.csv --describe
```

**3️⃣ Check missing values**

```bash
python data_explorer.py --file data/customers-100.csv --missing
```

**4️⃣ Show correlation matrix**

```bash
python data_explorer.py --file data/customers-100.csv --correlation
```

**5️⃣ Combine multiple analyses**

```bash
python data_explorer.py --file data/customers-100.csv --describe --missing
```

---

## 📊 Example Output

```
Loaded dataset with 100 rows and 12 columns.

📊 Dataset Description:
          Age       Income      Score
count   100.00      100.00      100.00
mean     35.22    55000.45       65.22
std       8.22     12000.30       18.76

❓ Missing Values:
Age        0
Income     2
Score      1
dtype: int64

🔗 Correlation Matrix:
              Age    Income    Score
Age         1.000    0.452   -0.231
Income      0.452    1.000    0.773
Score      -0.231    0.773    1.000
```

---

## 🧱 Tech Stack

* **Python 3.8+**
* **pandas**
* **argparse**

---

## 💡 Future Enhancements

* Add colorized output using `rich` or `colorama`
* Add support for JSON and Excel formats
* Add visualizations (histograms, heatmaps)
* Package and publish as a `pip` installable tool

---

## 📜 License

MIT License © 2025 Karthik Chimkode

---

## 🌟 Acknowledgements

Built as part of a **Machine Learning Foundations** project series — focusing on Python tool design, modular coding, and command-line interfaces for data science.

```

