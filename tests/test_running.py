from src.models.user import User
from src.models.activity import Activity
from src.engine.plan_generator import generate_plan


def test_running_plan_no_solids():
    user = User(
        weight_kg=70.0,
        level="intermediate",
        main_sport="running",
        digestive_tolerance="medium",
        sweat_profile="medium",
        available_container_types=["belt"],
    )

    activity = Activity(
        sport="running",
        duration_minutes=150,
        intensity_level="high",
        temperature_c=16.0,
        distance_km=32.0,
    )

    plan = generate_plan(user, activity)

    assert "solid" not in plan.recommended_formats
