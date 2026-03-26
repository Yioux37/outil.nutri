def get_sodium_target(
    sport: str,
    temperature_c: float,
    sweat_profile: str,
) -> float:
    base = {
        "trail": 600.0,
        "running": 500.0,
        "cycling": 700.0,
        "triathlon": 700.0,
    }.get(sport, 600.0)

    if temperature_c >= 20:
        base += 100.0
    if temperature_c >= 28:
        base += 100.0

    if sweat_profile == "medium":
        base += 50.0
    elif sweat_profile == "high":
        base += 150.0
    elif sweat_profile == "low":
        base -= 50.0

    return max(300.0, base)