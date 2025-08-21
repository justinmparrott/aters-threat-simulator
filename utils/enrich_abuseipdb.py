import requests

def enrich_abuseipdb(ip, api_key):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Key": api_key,
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90,
        "verbose": True
    }

    response = requests.get(url, headers=headers, params=params)
    try:
        data = response.json()
        return data.get("data", {})
    except Exception:
        return {"error": "AbuseIPDB failed"}
