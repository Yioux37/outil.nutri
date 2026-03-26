def get_risk_level(duration_minutes: int, intensity_level: str, temperature_c: float, digestive_tolerance: str) -> str:
    score = 0

    if duration_minutes >= 120:
        score += 1
    if duration_minutes >= 180:
        score += 1
    if duration_minutes >= 300:
        score += 1

    if intensity_level == "moderate":
        score += 1
    elif intensity_level == "high":
        score += 2

    if temperature_c >= 20:
        score += 1
    if temperature_c >= 28:
        score += 1

    if digestive_tolerance == "low":
        score += 2
    elif digestive_tolerance == "medium":
        score += 1

    if score <= 2:
        return "low"
    if score <= 5:
        return "medium"
    return "high"
