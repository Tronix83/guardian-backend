baseline = {}

def update_baseline(ip, risk_score):

    if ip not in baseline:
        baseline[ip] = {
            "count": 0,
            "avg_risk": 0
        }

    b = baseline[ip]

    b["count"] += 1
    b["avg_risk"] = (b["avg_risk"] * (b["count"] - 1) + risk_score) / b["count"]

    return b


def detect_anomaly(risk_score, baseline=50):

    if risk_score > 90 and b["avg_risk"] < 50:
        return {
            "anomaly": True,
            "type": "BEHAVIOR_SHIFT",
            "severity": "CRITICAL"
        }

    return {"anomaly": False}