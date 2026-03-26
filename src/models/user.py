from dataclasses import dataclass
from typing import List


@dataclass
class User:
    weight_kg: float
    level: str
    main_sport: str
    digestive_tolerance: str
    sweat_profile: str
    available_container_types: List[str]
    gut_training_level: str = "none"
    weekly_training_hours: float = 0.0
    longest_session_last_8_weeks: int = 0
