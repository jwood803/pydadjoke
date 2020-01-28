import fire
import requests
from typing import List

base_url = "https://icanhazdadjoke.com"
header = {
        "Accept": "application/json"
    }


def joke() -> str:
    resp = requests.get(base_url, headers=header)

    joke_json = resp.json()

    return joke_json["joke"]


def search(term: str) -> List[str]:
    url = f"{base_url}/search?term={term}&limit=10"

    resp = requests.get(url, headers=header)

    joke_json = resp.json()

    results = joke_json["results"]

    return [item["joke"] for item in results]


def main():
    fire.Fire({
        "joke": joke,
        "search": search,
        "list": list
    })
