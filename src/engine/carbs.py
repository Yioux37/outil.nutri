def get_carbs_target(
    sport: str,
    duration_minutes: int,
    intensity_level: str,
    digestive_tolerance: str,
    gut_training_level: str,
    weekly_training_hours: float,
    longest_session_last_8_weeks: int,
    level: str,
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

    gut_bonus = {
        "none": -5.0,
        "basic": 0.0,
        "moderate": 5.0,
        "advanced": 10.0,
    }.get(gut_training_level, 0.0)
    base += gut_bonus

    if weekly_training_hours >= 6:
        base += 2.5
    if weekly_training_hours >= 10:
        base += 2.5

    if longest_session_last_8_weeks >= 120:
        base += 2.5
    if longest_session_last_8_weeks >= 180:
        base += 2.5

    level_adjustment = {
        "beginner": -5.0,
        "intermediate": 0.0,
        "advanced": 2.5,
    }.get(level, 0.0)
    base += level_adjustment

    if weekly_training_hours < 4 and duration_minutes >= 180:
        base -= 7.5

    if longest_session_last_8_weeks < 90 and duration_minutes >= 240:
        base -= 5.0

    if gut_training_level == "none" and duration_minutes >= 180:
        base -= 5.0

    caps = {
        "trail": 60.0,
        "running": 60.0,
        "cycling": 90.0,
        "triathlon": 80.0,
    }

    if gut_training_level == "none":
        caps["cycling"] = min(caps["cycling"], 75.0)
        caps["triathlon"] = min(caps["triathlon"], 70.0)

    floor = 20.0
    ceiling = caps.get(sport, 60.0)

    return max(floor, min(base, ceiling))
