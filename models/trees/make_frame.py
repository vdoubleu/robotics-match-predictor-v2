import json
import pandas as pd

def make_dataframe():
    data_file = open(r"./data/cleanData.txt", "r+")
    df = pd.read_json(data_file.readline())
    data_file.close()
    return df

def make_flat_dataframe():
    data_file=open(r"./data/cleanData.txt", "r+")
    data = json.loads(data_file.readline())

    all_entries = []

    for entry in data:
        new_entry = {}

        for label in entry:
            if label == "redScore" or label == "blueScore":
                new_entry.update({label:entry[label]})
                continue

            for sublabel in entry[label]:
                new_sublabel = label+sublabel
                new_entry.update({new_sublabel:entry[label][sublabel]})

        all_entries.append(new_entry)

    df = pd.DataFrame(all_entries)
    return df


if __name__ == "__main__":
    flat = make_flat_dataframe()
    print(flat.columns)

