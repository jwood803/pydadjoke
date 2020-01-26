import fire
import requests


def joke():
    header = {
        "Accept": "application/json"
    }

    resp = requests.get("https://icanhazdadjoke.com/", headers=header)

    joke_json = resp.json()

    return joke_json["joke"]


if __name__ == "__main__":
    fire.Fire(joke)
