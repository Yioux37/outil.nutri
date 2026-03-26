from src.models.user import User
from src.models.activity import Activity
from src.engine.plan_generator import generate_plan


def test_packaging_short_effort_can_fit_without_refill():
    user = User(
        weight_kg=68.0,
        level="intermediate",
        main_sport="running",
        digestive_tolerance="medium",
        sweat_profile="low",
        available_container_types=["1x500ml_flask"],
        gut_training_level="basic",
        weekly_training_hours=5.0,
        longest_session_last_8_weeks=90,
    )

    activity = Activity(
        sport="running",
        duration_minutes=60,
        intensity_level="low",
        temperature_c=15.0,
        distance_km=10.0,
    )

    plan = generate_plan(user, activity)

    assert plan.total_fluids_ml <= 500
    assert any("without refill" in note.lower() for note in plan.packaging_notes)
