from src.models.user import User
from src.models.activity import Activity
from src.engine.plan_generator import generate_plan


def test_triathlon_plan_basic():
    user = User(
        weight_kg=72.0,
        level="advanced",
        main_sport="triathlon",
        digestive_tolerance="medium",
        sweat_profile="high",
        available_container_types=["2x750ml_bidons", "race_belt"],
    )

    activity = Activity(
        sport="triathlon",
        duration_minutes=300,
        intensity_level="moderate",
        temperature_c=24.0,
    )

    plan = generate_plan(user, activity)

    assert plan.sodium_mg_per_l >= 750
    assert "gel" in plan.recommended_formats
