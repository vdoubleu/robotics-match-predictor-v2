import json
import requests
from string import ascii_uppercase

"""
this collects data from the vexdb public database and formats the data into a json file
"""

CURR_YEAR = 20 #year set as 2020

def get_team_stats(team_id, team_season=None):
    """
    takes in string: the id/number of the team
    returns a dict: the information about the team

    the dict contains:
        - basic team info (where they come from, their name, registered?, etc.)(disabled because not providing useful info and reduces number of necessary calls)
        - age of team
        - age of organisation (currently disabled because it would take too long to run)
        - most recent season rating (vrating, vrating rank)
        - most recent season average team stats(wins/losses, CCWM, OPR/DPR, etc.)
    """
    
    basic_info = get_gen(team_id)
    team_age = get_team_age(team_id)
    #org_age = get_org_age(team_id)
    rating = get_rating(team_id, season=team_season)
    stats = get_stats(team_id, season=team_season)

    outDict = basic_info
    #outDict.update({"teamAge": team_age, "orgAge": org_age, "ratings": rating, "stats": stats})
    outDict.update({"teamAge": team_age, "ratings": rating, "stats": stats})

    return outDict


def get_gen(team_id):
    gen_url = "https://api.vexdb.io/v1/get_teams"
    gen_param = {"team": team_id}
    gen_res = (json.loads(requests.get(gen_url, gen_param).text))["result"][0]

    return gen_res

def get_team_age(team_id):
    age_url = "https://api.vexdb.io/v1/get_matches"
    age_param = {"team": team_id}
    age_out = json.loads(requests.get(age_url, age_param).text)

    age_res = int(age_out["result"][age_out["size"] - 1]["sku"][7:9])

    return CURR_YEAR - age_res

def get_org_age(team_id):
    if not team_id[-1].isnumeric():
        team_id = team_id[:-1]

    max_age = 0

    for char in ascii_uppercase:
        test_url = "https://api.vexdb.io/v1/get_matches"
        test_param = {"team": team_id + char}
        test_out = json.loads(requests.get(test_url, test_param).text)
        
        if test_out["size"] != 0:
            test_res = int(test_out["result"][test_out["size"] - 1]["sku"][7:9])
            max_age = max(max_age, CURR_YEAR - test_res)

    return max_age
   
def get_rating(team_id, season = None):
    rating_url = "https://api.vexdb.io/v1/get_season_rankings"

    if season is not None: 
        rating_param = {"team": team_id, "season": season}
    else:
        rating_param = {"team": team_id}

    rating_res = json.loads(requests.get(rating_url, rating_param).text)["result"]

    return rating_res

def get_stats(team_id, season = None):
    stat_url = "https://api.vexdb.io/v1/get_rankings"

    if season is not None:
        stat_param = {"team": team_id, "season": season}
    else:
        stat_param = {"team": team_id}

    stat_res = json.loads(requests.get(stat_url, stat_param).text)["result"]

    return stat_res

if __name__ == "__main__":
    print(get_team_stats("2327A", team_season="Tower Takeover"))
