from src.models.user import User
from src.models.activity import Activity
from src.engine.plan_generator import generate_plan


def test_advanced_gut_training_allows_higher_carbs():
    base_kwargs = dict(
        weight_kg=68.0,
        level="intermediate",
        main_sport="cycling",
        digestive_tolerance="medium",
        sweat_profile="medium",
        available_container_types=["2x750ml_bidons"],
        weekly_training_hours=8.0,
        longest_session_last_8_weeks=240,
    )

    low_gut_user = User(**base_kwargs, gut_training_level="none")
    high_gut_user = User(**base_kwargs, gut_training_level="advanced")

    activity = Activity(
        sport="cycling",
        duration_minutes=240,
        intensity_level="moderate",
        temperature_c=22.0,
    )

    low_plan = generate_plan(low_gut_user, activity)
    high_plan = generate_plan(high_gut_user, activity)

    assert high_plan.carbs_per_hour > low_plan.carbs_per_hour
