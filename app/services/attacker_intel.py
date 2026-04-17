import random


def analyze_ip(ip: str):
    fake_locations = [
        {"country": "US", "city": "New York"},
        {"country": "RU", "city": "Moscow"},
        {"country": "CH", "city": "Beijing"},
        {"country": "DE", "city": "Berlin"},
        {"country": "BR", "city": "Sao Paulo"},
    ]

    location = random.choice(fake_locations)

    score = random.randint(20, 100)

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