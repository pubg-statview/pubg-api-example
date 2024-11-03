import requests
from decouple import config

API_KEY = config('API_KEY')

def get_match_data(match_id):
    url = f"https://api.pubg.com/shards/kakao/matches/{match_id}"
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Accept': "application/vnd.api+json"
    }

    res = requests.get(url, headers=headers)
    return res.json()

def get_telemetry_url(match_dict):
    for item in match_dict.get("included", []):
        if item["type"] == "asset":
            return item["attributes"]["URL"]
        
    return None

def get_telemetry_data(url):
    res = requests.get(url)
    return res.json()

if __name__ == '__main__':
    match_dict = get_match_data("5f5ede2b-d16e-4364-a2f1-5fed5a137fd2")
    url = get_telemetry_url(match_dict)
    print(url)
    print(get_telemetry_data(url))
