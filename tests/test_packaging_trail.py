from src.models.user import User
from src.models.activity import Activity
from src.engine.plan_generator import generate_plan


def test_packaging_trail_estimates_flasks_and_gels():
    user = User(
        weight_kg=68.0,
        level="intermediate",
        main_sport="trail",
        digestive_tolerance="medium",
        sweat_profile="medium",
        available_container_types=["2x500ml_flasques"],
        gut_training_level="basic",
        weekly_training_hours=6.0,
        longest_session_last_8_weeks=180,
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

    assert plan.carrying_capacity_ml == 1000
    assert plan.estimated_bottles >= 3
    assert plan.estimated_gels >= 1
