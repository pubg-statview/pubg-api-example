import json
import requests

from decouple import config

API_KEY = config('API_KEY')
HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Accept': "application/vnd.api+json"
}

def save_json(j, filename="j.json"):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(j, f, indent=4, ensure_ascii=False)
    except:
        pass

if __name__ == '__main__':
    url = "https://telemetry-cdn.pubg.com/bluehole-pubg/kakao/2024/10/18/16/29/2b177796-8d6e-11ef-aae5-8e2d0dc0c1b1-telemetry.json"
    res = requests.get(url, headers=HEADERS)
    save_json(res.json(), "telemetry-example-normal.json")

