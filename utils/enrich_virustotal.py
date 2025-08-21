import requests

def enrich_virustotal(ip, api_key):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": api_key}

    response = requests.get(url, headers=headers)
    try:
        data = response.json()
        attributes = data.get("data", {}).get("attributes", {})
        return {
            "asn": attributes.get("asn"),
            "country": attributes.get("country"),
            "reputation": attributes.get("reputation"),
            "last_analysis_stats": attributes.get("last_analysis_stats", {}),
        }
    except Exception:
        return {"error": "VirusTotal failed"}
