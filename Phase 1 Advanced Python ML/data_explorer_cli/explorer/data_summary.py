class DataSummary:
    def __init__(self, data):
        self.data = data 
    
    def show_head(self, n = 5):
        print(self.data.head(n))
    
    def describe(self):
        print(self.data.describe(include="all"))

    def missing(self):
        print(self.data.isnull().sum())

    def correlation(self):
        print(self.data.corr(numeric_only=True))
