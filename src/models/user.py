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