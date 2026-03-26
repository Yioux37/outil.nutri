def get_fluids_target(sport: str, temperature_c: float) -> float:
    base = {
        "trail": 650.0,
        "running": 550.0,
        "cycling": 700.0,
        "triathlon": 650.0,
    }.get(sport, 600.0)

    if temperature_c > 20:
        base += (temperature_c - 20) * 20.0

    return base