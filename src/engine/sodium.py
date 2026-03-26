def get_sodium_target(sport: str, sweat_profile: str) -> float:
    base = {
        "trail": 650.0,
        "running": 550.0,
        "cycling": 800.0,
        "triathlon": 750.0,
    }.get(sport, 600.0)

    if sweat_profile == "high":
        base += 150.0
    elif sweat_profile == "low":
        base -= 100.0

    return max(base, 300.0)