import requests


def analyze_ip(ip: str):

    geo = res.json()

    score = 0

    location = {
        "country": geo.get("country_name", "Unknown"),
        "city": geo.get("city", "Unknown"),
        "region": geo.get("region", "Unknown"),
        "org": geo.get("org", "Unknown"),
    }

    try:
        res = requests.get(f"https://ipapi.co/{ip}/json/", timeout=2)
        
        if res.status_code == 200:

            score = 50 + (hash(ip) % 50)  # Simple deterministic score based on IP hash

            geo = res.json()

            location = {
                "country": geo.get("country_name", "Unknown"),
                "city": geo.get("city", "Unknown"),
                "region": geo.get("region", "Unknown"),
                "org": geo.get("org", "Unknown"),
          }      

    except Exception:
        print("Geo lookup failed for", ip)

        ip_hash = hash(ip)

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

    
