from src.models.user import User
from src.models.activity import Activity
from src.engine.plan_generator import generate_plan


def test_packaging_cycling_requires_refill():
    user = User(
        weight_kg=63.0,
        level="intermediate",
        main_sport="cycling",
        digestive_tolerance="medium",
        sweat_profile="medium",
        available_container_types=["2x750ml_bidons"],
        gut_training_level="moderate",
        weekly_training_hours=8.0,
        longest_session_last_8_weeks=240,
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

    assert plan.total_fluids_ml >= 3500
    assert plan.carrying_capacity_ml == 1500
    assert plan.estimated_bottles >= 5
    assert any("refill required" in note.lower() for note in plan.packaging_notes)
