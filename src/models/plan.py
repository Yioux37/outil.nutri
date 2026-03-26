from dataclasses import dataclass
from typing import List


@dataclass
class Plan:
    carbs_per_hour: float
    fluids_ml_per_hour: float
    sodium_mg_per_l: float
    recommended_formats: List[str]
    risk_level: str