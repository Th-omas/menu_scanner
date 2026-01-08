import requests
import os

API_KEY = os.getenv("GOOGLE_API_KEY")
CX = os.getenv("GOOGLE_CX_ID")

def search_image(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query + " food dish",
        "searchType": "image",
        "num": 1,
        "key": API_KEY,
        "cx": CX
    }
    r = requests.get(url, params=params).json()
    try:
        return r["items"][0]["link"]
    except:
        return None
