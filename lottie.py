import json
import requests


def load_lottie_url(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)