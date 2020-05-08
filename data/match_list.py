import json
import requests
import sys

"""
gathers a list of all the matches played in the given season
"""

def get_match_list(season, f_num):
    start = 5000 * f_num
    MATCH_COUNT_CAP = start+5000

    match_url = "https://api.vexdb.io/v1/get_matches"
    
    match_lst = []

    totalNum = json.loads(requests.get(match_url, {"nodata": "true"}).text)["size"]

    while True:
        match_params = {"season": season, "limit_start": start, "scored": 1}
        match_out = json.loads(requests.get(match_url, match_params).text)

        if match_out["size"] == 0 or start >= MATCH_COUNT_CAP:
            break

        match_lst.extend(match_out["result"])

        print(str(start) + "/" + str(totalNum))
        start = start + 5000
    return match_lst

if __name__ == "__main__":
    arg_num = len(sys.argv)
    if arg_num > 1:
        file_num = sys.argv[1]
    else:
        print("no file num was inputed, defaulting to zero")
        file_num = 0

    team_file = open(r"./data_files/match" + file_num + ".txt", "w+")
    SEASON_NAME = "Tower Takeover"

    team_file.write(json.dumps(get_match_list(SEASON_NAME, int(file_num))))

    team_file.close()
