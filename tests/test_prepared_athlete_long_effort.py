from src.models.user import User
from src.models.activity import Activity
from src.engine.plan_generator import generate_plan


def test_prepared_athlete_long_effort_can_target_higher_carbs():
    user = User(
        weight_kg=69.0,
        level="advanced",
        main_sport="trail",
        digestive_tolerance="high",
        sweat_profile="medium",
        available_container_types=["2x500ml_flasques", "vest"],
        gut_training_level="advanced",
        weekly_training_hours=10.0,
        longest_session_last_8_weeks=300,
    )

    activity = Activity(
        sport="trail",
        duration_minutes=300,
        intensity_level="moderate",
        temperature_c=20.0,
        distance_km=35.0,
        elevation_gain_m=1800.0,
    )

    plan = generate_plan(user, activity)

    assert plan.carbs_per_hour >= 55
