import requests

def get_geo(ip: str):

    try:
        # simple free geo lookup
        res = requests.get(f"http://ip-api.com/json/{ip}")
        data = res.json()

        return {
            "country": data.get("country", "UNKNOWN"),
            "region": data.get("regionName", "UNKNOWN"),
            "city": data.get("city", "UNKNOWN"),
            "isp": data.get("isp", "UNKNOWN")
        }

    except Exception:
        return {
            "country": "UNKNOWN",
            "region": "UNKNOWN",
            "city": "UNKNOWN",
            "isp": "UNKNOWN"
        }