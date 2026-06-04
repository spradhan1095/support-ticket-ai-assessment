import pandas as pd
from config import CSV_PATH


class DataLoader:

    def __init__(self):
        self.df = self.load_data()

    def load_data(self):

        df = pd.read_csv(CSV_PATH)

        df["created_at"] = pd.to_datetime(
            df["created_at"]
        )

        return df


data_loader = DataLoader()