from dataclasses import dataclass
from typing import Optional


@dataclass
class Activity:
    sport: str
    duration_minutes: int
    intensity_level: str
    temperature_c: float
    distance_km: Optional[float] = None
    elevation_gain_m: Optional[float] = None