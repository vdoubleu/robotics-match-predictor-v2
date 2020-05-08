import json
import sys


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("no arguments were listed")
        sys.exit()


    file_nums = sys.argv[1:]

    out = []

    for num in file_nums:
        f = open(r"./data_files/simpData" + num + ".txt", "r+")
        out = out + json.loads(f.readline())
        f.close()

    clean_file = open(r"./data_files/cleanData.txt", "w+")
    clean_file.write(json.dumps(out))
    clean_file.close()

