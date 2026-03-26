def get_risk_level(duration_minutes: int, intensity_level: str, temperature_c: float, digestive_tolerance: str) -> str:
    score = 0

    if duration_minutes >= 180:
        score += 1
    if duration_minutes >= 300:
        score += 1
    if intensity_level == "high":
        score += 1
    if temperature_c >= 25:
        score += 1
    if digestive_tolerance == "low":
        score += 2

    if score <= 1:
        return "low"
    if score <= 3:
        return "medium"
    return "high"