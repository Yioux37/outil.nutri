from src.models.user import User
from src.models.activity import Activity
from src.engine.plan_generator import generate_plan


def test_low_digestive_tolerance_reduces_aggressiveness():
    user = User(
        weight_kg=65.0,
        level="intermediate",
        main_sport="cycling",
        digestive_tolerance="low",
        sweat_profile="medium",
        available_container_types=["2x750ml_bidons"],
    )

    activity = Activity(
        sport="cycling",
        duration_minutes=240,
        intensity_level="high",
        temperature_c=22.0,
    )

    plan = generate_plan(user, activity)

    assert plan.carbs_per_hour <= 75
    assert "solid" not in plan.recommended_formats
    assert plan.risk_level in ["medium", "high"]
