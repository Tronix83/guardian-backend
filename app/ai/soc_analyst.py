def analyze_event(event: dict):
    data = event.get("data", {})

    ip = data.get("ip", "unknown")
    geo = data.get("geo", {})
    score = data.get("threat_score", 0)
    behavior = data.get("behavior", "LOW")

    summary = []

    if level == "CRITICAL":
        summary.append("Active high-confidence intrusion detected.")
    elif level == "HIGH":
        summary.append("Suspicious aggressive activity observed.")
    else:
        summary.append("Low-level scanning or noise detected.")

    if behavior == "BRUTE FORCE":
        summary.append("Pattern indicates repeated authentication attempts.")
    elif behavior == "RECONNAISSANCE":
        summary.append("Network probing behavior detected.")
    
    if geo.get("country") not in ["United States", "Unknown"]:
        summary.append(f"Foreign-origin traffic from {geo.get('country')}.")
    
    if score > 85:
        action = "IMMEDIATE BLOCK + ESCALATE INCIDENT"
    elif score > 60:
        action = "MONITOR CLOSELY + ALERT SOC TEAM"
    elif score > 40:
        action = "LOG AND REVIEW"
    else:
        action = "NO ACTION NEEDED"
    
    return {
        "ip": ip,   
        "summary": " ".join(summary),
        "recommended_action": action,
        "threat_score": score,
        "threat_level": level,
        "behavior": behavior,
        "confidence": min(0.99, score / 100 + 0.1)  # Simple confidence calculation
    }