import argparse
from explorer.dataset_loader import DatasetLoader
from explorer.data_summary import DataSummary

class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Data Explorer CLI TOOL")
        self.parser.add_argument("--file", required=True, help="Path to csv file")
        self.parser.add_argument("--head", action="store_true", help="show first five dataset description")
        self.parser.add_argument("--describe", action="store_true", help="Show dataset description")
        self.parser.add_argument("--missing", action="store_true", help="Show Missing values count")
        self.parser.add_argument("--correlation", action="store_true", help="Show correlation matrix")

    def run(self):
        args = self.parser.parse_args()
        loader = DatasetLoader(args.file)
        data = loader.load()
        if data is None:
            return
        
        summary = DataSummary(data)

        if args.head:
            summary.show_head()
        elif args.describe:
            summary.describe()
        elif args.missing:
            summary.missing()
        elif args.correlation:
            summary.correlation()
        else:
            print("No action specified. Try --help to see available commads.")