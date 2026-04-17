import random
import requests


def analyze_ip(ip: str):

    try:

        res = requests.get(f"https://ipapi.co/{ip}/json/", timeout=2)
        geo = res.json()

        location = {
            "country": geo.get("country_name", "Unknown"),
            "city": geo.get("city", "Unknown"),
            "region": geo.get("region", "Unknown"),
            "org": geo.get("org", "Unknown"),
        }

    except Exception:

        location = {
            "country": "Unknown",
            "city": "Unkown",
            "region": "Unknown",
            "org": "Unknown",
        }

        ip_hash = sum([ord(c) for c in ip])

        score = (ip_hash % 100)

        
    if score > 85:
        level = "CRITICAL"
    elif score > 60:
        level = "HIGH"
    elif score > 40:
        level = "MEDIUM"
    else:
        level = "LOW"
    
    behavior = (
        "BRUTE FORCE" if score > 80 else
        "RECONNAISSANCE" if score > 50
        else 
        "NORMAL TRAFFIC"
    )

    return {
        "ip": ip,
        "geo": location,
        "threat_score": score,
        "threat_level": level,
        "behavior": behavior
    }

    
