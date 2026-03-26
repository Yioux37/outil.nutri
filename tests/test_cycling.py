from src.models.user import User
from src.models.activity import Activity
from src.engine.plan_generator import generate_plan


def test_cycling_plan_basic():
    user = User(
        weight_kg=63.0,
        level="intermediate",
        main_sport="cycling",
        digestive_tolerance="medium",
        sweat_profile="medium",
        available_container_types=["2x750ml_bidons"],
    )

    activity = Activity(
        sport="cycling",
        duration_minutes=240,
        intensity_level="moderate",
        temperature_c=22.0,
        distance_km=110.0,
        elevation_gain_m=1800.0,
    )

    plan = generate_plan(user, activity)

    assert plan.carbs_per_hour >= 60
    assert plan.fluids_ml_per_hour >= 700
    assert plan.sodium_mg_per_l >= 600
    assert "liquid" in plan.recommended_formats
