import json


if __name__ == "__main__":
    f = open(r"./data_files/match2.txt", "r+")

    data = json.loads(f.readline())

    print(data[927])
