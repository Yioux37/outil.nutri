from src.models.user import User
from src.models.activity import Activity
from src.engine.plan_generator import generate_plan


def test_hot_conditions_increase_fluids_and_sodium():
    user = User(
        weight_kg=70.0,
        level="intermediate",
        main_sport="running",
        digestive_tolerance="medium",
        sweat_profile="high",
        available_container_types=["belt"],
    )

    activity = Activity(
        sport="running",
        duration_minutes=150,
        intensity_level="moderate",
        temperature_c=30.0,
        distance_km=28.0,
    )

    plan = generate_plan(user, activity)

    assert plan.fluids_ml_per_hour >= 700
    assert plan.sodium_mg_per_l >= 700
