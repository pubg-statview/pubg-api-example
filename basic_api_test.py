import json
import requests

from decouple import config

API_KEY = config('API_KEY')
HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Accept': "application/vnd.api+json"
}

def get_user_info(username):
    url = "https://api.pubg.com/shards/kakao/players"
    params = {
        'filter[playerNames]': username
    }
    res = requests.get(url=url, headers=HEADERS, params=params)
    return res.json()

def get_user_histories(j):
    try:
        return j['data'][0]["relationships"]["matches"]["data"]
    except:
        print("!!")

def get_match_history(matchid):
    url = f"https://api.pubg.com/shards/kakao/matches/{matchid}"
    res = requests.get(url=url, headers=HEADERS)
    return res.json()

def get_lifetime(playerid="account.a164c65de7bd46f3a0101d4b8ad4a626"):
    url = "https://api.pubg.com/shards/kakao/seasons/lifetime/gameMode/squad/players"
    params = {
        'filter[playerIds]' : playerid
    }
    res = requests.get(url=url, headers=HEADERS, params=params)
    return res.json()

def get_weapon_mastery(playerid="account.a164c65de7bd46f3a0101d4b8ad4a626"):
    url = f"https://api.pubg.com/shards/kakao/players/{playerid}/weapon_mastery"
    res = requests.get(url=url, headers=HEADERS)
    return res.json()


def get_survival_mastery(playerid="account.a164c65de7bd46f3a0101d4b8ad4a626"):
    url = f"https://api.pubg.com/shards/kakao/players/{playerid}/survival_mastery"
    res = requests.get(url=url, headers=HEADERS)
    return res.json()


def json_printer(j):
    json_string = json.dumps(j, indent=4, ensure_ascii=False)
    print(json_string)

def save_json(j, filename="j.json"):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(j, f, indent=4, ensure_ascii=False)
    except:
        pass

if __name__ == '__main__':
    # info = get_user_info("Lil_Ziu__Vert")
    # save_json(info, 'players-api-example-6.json')

    # # info = get_user_info("Geiwokankantui-")
    # # save_json(info, 'players-api-example-solo-user.json')

    history = get_match_history("ff322e9b-689f-4534-8592-fc38cb0f0549")
    save_json(history, 'match-history-example-arcade-2.json')
    
