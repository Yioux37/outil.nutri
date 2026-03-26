from src.models.user import User
from src.models.activity import Activity
from src.engine.plan_generator import generate_plan


def test_packaging_capacity_warning_for_long_hot_effort():
    user = User(
        weight_kg=70.0,
        level="intermediate",
        main_sport="cycling",
        digestive_tolerance="medium",
        sweat_profile="high",
        available_container_types=["1x500ml_bidon"],
        gut_training_level="basic",
        weekly_training_hours=6.0,
        longest_session_last_8_weeks=180,
    )

    activity = Activity(
        sport="cycling",
        duration_minutes=300,
        intensity_level="moderate",
        temperature_c=28.0,
        distance_km=140.0,
        elevation_gain_m=2200.0,
    )

    plan = generate_plan(user, activity)

    assert plan.carrying_capacity_ml == 500
    assert any("refill required" in note.lower() for note in plan.packaging_notes)
