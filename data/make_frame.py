import json
import pandas as pd

def make_dataframe():
    data_file = open(r"./data.txt", "r+")

    df = pd.read_json(data_file.readline())

    print(df.iloc[0]["red1"])

if __name__ == "__main__":
    make_dataframe()
