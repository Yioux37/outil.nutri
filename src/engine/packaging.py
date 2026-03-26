import math
import re
from typing import List


def extract_carrying_capacity_ml(container_types: List[str]) -> int:
    total = 0

    for item in container_types:
        match = re.search(r"(\d+)x(\d+)ml", item.lower())
        if match:
            quantity = int(match.group(1))
            volume_ml = int(match.group(2))
            total += quantity * volume_ml

    return total


def get_default_unit_volume_ml(sport: str) -> int:
    if sport in {"cycling", "triathlon"}:
        return 750
    return 500


def get_drink_mix_concentration_g_per_l(sport: str) -> float:
    if sport in {"cycling", "triathlon"}:
        return 60.0
    return 50.0


def build_packaging_plan(
    sport: str,
    duration_minutes: int,
    carbs_per_hour: float,
    fluids_ml_per_hour: float,
    available_container_types: List[str],
) -> dict:
    duration_hours = duration_minutes / 60.0

    total_fluids_ml = round(fluids_ml_per_hour * duration_hours, 1)
    total_carbs_g = round(carbs_per_hour * duration_hours, 1)

    carrying_capacity_ml = extract_carrying_capacity_ml(available_container_types)
    unit_volume_ml = get_default_unit_volume_ml(sport)
    estimated_bottles = math.ceil(total_fluids_ml / unit_volume_ml)

    drink_concentration = get_drink_mix_concentration_g_per_l(sport)

    if sport in {"cycling", "triathlon"}:
        target_carbs_from_fluids = total_carbs_g * 0.6
    else:
        target_carbs_from_fluids = total_carbs_g * 0.5

    if carrying_capacity_ml > 0:
        possible_carbs_from_carried_fluids = (carrying_capacity_ml / 1000) * drink_concentration
    else:
        possible_carbs_from_carried_fluids = target_carbs_from_fluids

    carbs_from_fluids = min(target_carbs_from_fluids, possible_carbs_from_carried_fluids)
    remaining_carbs = max(total_carbs_g - carbs_from_fluids, 0.0)
    estimated_gels = math.ceil(remaining_carbs / 25.0) if remaining_carbs > 0 else 0

    packaging_notes: List[str] = []

    if carrying_capacity_ml == 0:
        packaging_notes.append("Container capacity unknown: packaging estimate is approximate.")
    elif carrying_capacity_ml < total_fluids_ml:
        packaging_notes.append("Carrying capacity insufficient for full fluid target: refill required.")
    else:
        packaging_notes.append("Carrying capacity covers fluid target without refill.")

    if estimated_gels > 0:
        packaging_notes.append(f"Estimated gels needed: {estimated_gels}.")
    if estimated_gels >= 6:
        packaging_notes.append("High gel count: consider more drink mix or planned refills.")

    return {
        "total_fluids_ml": total_fluids_ml,
        "total_carbs_g": total_carbs_g,
        "carrying_capacity_ml": carrying_capacity_ml,
        "estimated_gels": estimated_gels,
        "estimated_bottles": estimated_bottles,
        "packaging_notes": packaging_notes,
    }
