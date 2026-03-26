from src.models.user import User
from src.models.activity import Activity
from src.engine.plan_generator import generate_plan


def test_short_effort_stays_lower():
    user = User(
        weight_kg=68.0,
        level="intermediate",
        main_sport="running",
        digestive_tolerance="medium",
        sweat_profile="low",
        available_container_types=["belt"],
    )

    activity = Activity(
        sport="running",
        duration_minutes=60,
        intensity_level="low",
        temperature_c=15.0,
        distance_km=10.0,
    )

    plan = generate_plan(user, activity)

    assert plan.carbs_per_hour <= 45
    assert plan.fluids_ml_per_hour <= 550
    assert plan.sodium_mg_per_l <= 500
