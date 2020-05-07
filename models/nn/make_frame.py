import json
import pandas as pd

def make_dataframe():
    data_file = open(r"./data/simpData.txt", "r+")
    df = pd.read_json(data_file.readline())
    data_file.close()
    return df

def make_flat_dataframe():
    data_file=open(r"./data/simpData.txt", "r+")
    data = json.loads(data_file.readline())

    flattened = list(map(lambda entry: entry["red1"].update(entry["red2"]).update(entry["blue1"]).update(entry["blue2"]).update({"redScore": entry["redScore"], "blueScore": entry["blueScore"]}), data))

    df = pd.DataFram(flattened)
    return df


if __name__ == "__main__":
    print(make_dataframe())
