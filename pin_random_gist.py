import os
import random
import requests

GITHUB_API = "https://api.github.com"
GITHUB_USERNAME = os.environ.get("GITHUB_USERNAME")
GITHUB_TOKEN = os.environ.get("GH_TOKEN")

if not GITHUB_TOKEN:
    raise Exception("GH_TOKEN environment variable not set.")
if not GITHUB_USERNAME:
    raise Exception("GITHUB_USERNAME environment variable not set.")

def get_gists():
    url = f"{GITHUB_API}/users/{GITHUB_USERNAME}/gists"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def pin_gist(gist_id):
    url = f"{GITHUB_API}/gists/{gist_id}/star"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.put(url, headers=headers)
    response.raise_for_status()

def main():
    gists = get_gists()
    if not gists:
        print("No gists found.")
        return
    random_gist = random.choice(gists)
    pin_gist(random_gist["id"])
    print(f"Pinned gist: {random_gist['html_url']}")

if __name__ == "__main__":
    main()
