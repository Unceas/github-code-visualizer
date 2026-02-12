# app/github_client.py
import requests

class GitHubFetchError(Exception):
    pass

def fetch_code_from_raw_url(url: str) -> str:
    resp = requests.get(url, timeout=10)
    if resp.status_code != 200:
        raise GitHubFetchError(
            f"Failed to fetch file. Status: {resp.status_code}"
        )
    return resp.text
