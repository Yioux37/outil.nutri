from src.models.user import User
from src.models.activity import Activity
from src.engine.plan_generator import generate_plan


def test_higher_training_load_supports_higher_carbs():
    low_load_user = User(
        weight_kg=70.0,
        level="intermediate",
        main_sport="cycling",
        digestive_tolerance="medium",
        sweat_profile="medium",
        available_container_types=["2x750ml_bidons"],
        gut_training_level="basic",
        weekly_training_hours=3.0,
        longest_session_last_8_weeks=90,
    )

    high_load_user = User(
        weight_kg=70.0,
        level="intermediate",
        main_sport="cycling",
        digestive_tolerance="medium",
        sweat_profile="medium",
        available_container_types=["2x750ml_bidons"],
        gut_training_level="basic",
        weekly_training_hours=10.0,
        longest_session_last_8_weeks=240,
    )

    activity = Activity(
        sport="cycling",
        duration_minutes=240,
        intensity_level="moderate",
        temperature_c=22.0,
    )

    low_plan = generate_plan(low_load_user, activity)
    high_plan = generate_plan(high_load_user, activity)

    assert high_plan.carbs_per_hour > low_plan.carbs_per_hour
