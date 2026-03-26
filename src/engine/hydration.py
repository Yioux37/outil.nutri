def get_fluids_target(
    sport: str,
    temperature_c: float,
    duration_minutes: int,
    sweat_profile: str,
) -> float:
    base = {
        "trail": 550.0,
        "running": 500.0,
        "cycling": 650.0,
        "triathlon": 600.0,
    }.get(sport, 550.0)

    if duration_minutes >= 120:
        base += 50.0
    if duration_minutes >= 240:
        base += 50.0

    if temperature_c >= 20:
        base += 100.0
    if temperature_c >= 28:
        base += 100.0

    if sweat_profile == "medium":
        base += 50.0
    elif sweat_profile == "high":
        base += 120.0

    return max(300.0, base)