from src.models.user import User
from src.models.activity import Activity
from src.engine.plan_generator import generate_plan


def test_very_long_effort_pushes_higher_targets():
    user = User(
        weight_kg=72.0,
        level="advanced",
        main_sport="trail",
        digestive_tolerance="high",
        sweat_profile="high",
        available_container_types=["2x500ml_flasques", "vest"],
    )

    activity = Activity(
        sport="trail",
        duration_minutes=420,
        intensity_level="moderate",
        temperature_c=26.0,
        distance_km=60.0,
        elevation_gain_m=3200.0,
    )

    plan = generate_plan(user, activity)

    assert plan.carbs_per_hour >= 50
    assert plan.fluids_ml_per_hour >= 800
    assert plan.sodium_mg_per_l >= 800
    assert plan.risk_level in ["medium", "high"]
