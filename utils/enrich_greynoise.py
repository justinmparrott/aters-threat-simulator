import requests

def enrich_greynoise(ip, api_key):
    url = f"https://api.greynoise.io/v3/community/{ip}"
    headers = {"key": api_key}

    response = requests.get(url, headers=headers)
    try:
        data = response.json()
        return {
            "classification": data.get("classification"),
            "name": data.get("name"),
            "noise": data.get("noise"),
            "riot": data.get("riot"),
            "link": data.get("link"),
        }
    except Exception:
        return {"error": "GreyNoise failed"}
