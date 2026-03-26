def get_carbs_target(sport: str, intensity_level: str, digestive_tolerance: str) -> float:
    base = {
        "trail": 50.0,
        "running": 45.0,
        "cycling": 75.0,
        "triathlon": 65.0,
    }.get(sport, 50.0)

    if intensity_level == "high":
        base -= 5.0

    if digestive_tolerance == "low":
        base -= 10.0
    elif digestive_tolerance == "high":
        base += 5.0

    return max(base, 20.0)