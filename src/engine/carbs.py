def get_carbs_target(
    sport: str,
    duration_minutes: int,
    intensity_level: str,
    digestive_tolerance: str,
) -> float:
    base = {
        "trail": 45.0,
        "running": 40.0,
        "cycling": 65.0,
        "triathlon": 55.0,
    }.get(sport, 45.0)

    if duration_minutes >= 90:
        base += 5.0
    if duration_minutes >= 180:
        base += 5.0
    if duration_minutes >= 300:
        base += 5.0

    if intensity_level == "moderate":
        base += 5.0
    elif intensity_level == "high":
        base += 10.0

    if digestive_tolerance == "low":
        base -= 10.0
    elif digestive_tolerance == "high":
        base += 5.0

    caps = {
        "trail": 60.0,
        "running": 60.0,
        "cycling": 90.0,
        "triathlon": 80.0,
    }

    floor = 20.0
    ceiling = caps.get(sport, 60.0)

    return max(floor, min(base, ceiling))