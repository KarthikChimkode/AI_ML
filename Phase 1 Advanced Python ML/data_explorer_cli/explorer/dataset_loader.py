import pandas as pd

class DatasetLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load(self):
        try:
            self.data = pd.read_csv(self.file_path)
            print(f"Loaded sataset with {self.data.shape[0]} rows and {self.data.shape[1]} colums.")
        except FileNotFoundError:
            print("File not found please provide valid csv path")
        except Exception as e:
            print(f"Error loading file : {e}")
        return self.data
    
        