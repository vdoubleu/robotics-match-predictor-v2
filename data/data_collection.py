import json
import requests

from team_data import get_team_stats

def get_data(team_file, season = None):
    matches = json.loads(team_file.readline())
    
    data = []

    for entry in matches:
        red1_info = get_team_stats(entry["red1"], team_season = season)
        red2_info = get_team_stats(entry["red2"], team_season = season)
        blue1_info = get_team_stats(entry["blue1"], team_season = season)
        blue2_info = get_team_stats(entry["blue2"], team_season = season)
        
        red_score = entry["redScore"]
        blue_score = entry["blueScore"]

        data.append({"red1": red1_info, "red2": red2_info, "blue1": blue1_info, "blue2": blue2_info, "redScore": red_score, "blueScore": blue_score})

    return data


if __name__ == "__main__":
    data_file = open(r"./data.txt", "w+")
    team_file = open(r"./match.txt", "r+")
    
    data_file.write(json.dumps(get_data(team_file, "Tower Takeover")))

    team_file.close()
    data_file.close()
