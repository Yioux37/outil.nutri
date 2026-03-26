from src.engine.carbs import get_carbs_target
from src.engine.hydration import get_fluids_target
from src.engine.sodium import get_sodium_target
from src.engine.digestion import get_risk_level
from src.models.plan import Plan
from src.models.user import User
from src.models.activity import Activity


def get_recommended_formats(sport: str, digestive_tolerance: str) -> list[str]:
    if sport == "cycling":
        return ["liquid", "gel", "solid"] if digestive_tolerance != "low" else ["liquid", "gel"]
    if sport == "trail":
        return ["liquid", "gel", "puree"]
    if sport == "running":
        return ["liquid", "gel"]
    if sport == "triathlon":
        return ["liquid", "gel"]
    return ["liquid", "gel"]


def generate_plan(user: User, activity: Activity) -> Plan:
    carbs = get_carbs_target(
        activity.sport,
        activity.duration_minutes,
        activity.intensity_level,
        user.digestive_tolerance,
    )

    fluids = get_fluids_target(
        activity.sport,
        activity.temperature_c,
        activity.duration_minutes,
        user.sweat_profile,
    )

    sodium = get_sodium_target(
        activity.sport,
        activity.temperature_c,
        user.sweat_profile,
    )

    risk = get_risk_level(
        activity.duration_minutes,
        activity.intensity_level,
        activity.temperature_c,
        user.digestive_tolerance,
    )

    formats = get_recommended_formats(activity.sport, user.digestive_tolerance)

    return Plan(
        carbs_per_hour=carbs,
        fluids_ml_per_hour=fluids,
        sodium_mg_per_l=sodium,
        recommended_formats=formats,
        risk_level=risk,
    )
