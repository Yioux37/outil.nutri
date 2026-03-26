from src.models.user import User
from src.models.activity import Activity
from src.engine.plan_generator import generate_plan


def test_underprepared_athlete_stays_more_conservative():
    user = User(
        weight_kg=69.0,
        level="beginner",
        main_sport="trail",
        digestive_tolerance="medium",
        sweat_profile="medium",
        available_container_types=["2x500ml_flasques"],
        gut_training_level="none",
        weekly_training_hours=2.5,
        longest_session_last_8_weeks=75,
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

    assert plan.carbs_per_hour <= 50
