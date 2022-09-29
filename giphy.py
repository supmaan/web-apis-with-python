import requests

API_KEY = "nA9LKF3LCDhBxjreeMft0MgA7lS5EPhy"
endpoint = "https://api.giphy.com/v1/gifs/trending"

params = {"api_key": API_KEY, "limit": 3, "rating": "g"}
response = requests.get(endpoint, params=params).json()
for gif in response["data"]:
    title = gif["title"]
    trending_date = gif["trending_datetime"]
    url = gif["url"]
    print(f"{title} | {trending_date} | {url}")