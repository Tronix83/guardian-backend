import requests


import requests

def analyze_ip(ip: str):

    # 🧠 ALWAYS DEFINE FIRST (prevents crash)
    geo = {}

    try:
        res = requests.get(
            f"https://ipapi.co/{ip}/json/",
            timeout=1
        )

        if res.status_code == 200:
            geo = res.json()

    except Exception as e:
        print("Geo lookup failed:", e)

    # 🌍 SAFE ACCESS (never crashes now)
    location = {
        "country": geo.get("country_name", "Unknown"),
        "city": geo.get("city", "Unknown"),
        "region": geo.get("region", "Unknown"),
        "org": geo.get("org", "Unknown"),
    }

    score = sum(ord(c) for c in ip) % 100

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
        "RECONNAISSANCE" if score > 50 else
        "NORMAL TRAFFIC"
    )

    return {
        "ip": ip,
        "geo": location,
        "threat_score": score,
        "threat_level": level,
        "behavior": behavior
    }

    
