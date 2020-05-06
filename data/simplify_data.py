import json
import statistics

def simp(lst):
    keys = ["rank", "wins", "losses", "ties", "wp", "ap", "sp", "trsp", "max_score", "opr", "dpr", "ccwm"]
    return dict((key, statistics.mean(map(lambda d: d[key], lst))) for key in keys)


data_file = open(r"./data.txt", "r+")
data = json.loads(data_file.readline())

res = []

for entry in data:
    if entry["red1"]["program"] == "VEXU":
        continue

    red1_data = {"teamAge": entry["red1"]["teamAge"], "vrating_rank": entry["red1"]["ratings"][0]["vrating_rank"], "vrating": entry["red1"]["ratings"][0]["vrating"]}
    red1_data.update(simp(entry["red1"]["stats"]))

    red2_data = {"teamAge": entry["red2"]["teamAge"], "vrating_rank": entry["red2"]["ratings"][0]["vrating_rank"], "vrating": entry["red2"]["ratings"][0]["vrating"]}
    red2_data.update(simp(entry["red2"]["stats"]))

    blue1_data = {"teamAge": entry["blue1"]["teamAge"], "vrating_rank": entry["blue1"]["ratings"][0]["vrating_rank"], "vrating": entry["blue1"]["ratings"][0]["vrating"]}
    blue1_data.update(simp(entry["blue1"]["stats"]))

    blue2_data = {"teamAge": entry["blue2"]["teamAge"], "vrating_rank": entry["blue2"]["ratings"][0]["vrating_rank"], "vrating": entry["blue2"]["ratings"][0]["vrating"]}
    blue2_data.update(simp(entry["blue2"]["stats"]))


    newDict = {"red1": red1_data, "red2": red2_data, "blue1": blue1_data, "blue2": blue2_data, "redScore": entry["redScore"], "blueScore": entry["blueScore"]}

    res.append(newDict)

simp_data_file = open(r"./simpData.txt", "w+")
simp_data_file.write(json.dumps(res))

simp_data_file.close()
data_file.close()
