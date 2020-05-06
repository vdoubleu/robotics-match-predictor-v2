import json
import requests

"""
gathers a list of all the matches played in the given season
"""

MATCH_COUNT_CAP = 5000


def get_match_list(season):
    start = 0

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
    team_file = open(r"./match.txt", "w+")
    SEASON_NAME = "Tower Takeover"

    team_file.write(json.dumps(get_match_list(SEASON_NAME)))

    team_file.close()
