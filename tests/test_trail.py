from src.models.user import User
from src.models.activity import Activity
from src.engine.plan_generator import generate_plan


def test_trail_plan_formats():
    user = User(
        weight_kg=68.0,
        level="intermediate",
        main_sport="trail",
        digestive_tolerance="medium",
        sweat_profile="medium",
        available_container_types=["2x500ml_flasques"],
    )

    activity = Activity(
        sport="trail",
        duration_minutes=180,
        intensity_level="moderate",
        temperature_c=18.0,
        distance_km=25.0,
        elevation_gain_m=1400.0,
    )

    plan = generate_plan(user, activity)

    assert "puree" in plan.recommended_formats
    assert plan.carbs_per_hour <= 60
