from src.models.user import User
from src.models.activity import Activity
from src.engine.plan_generator import generate_plan


def main() -> None:
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

    print("=== Outil.Nutri ===")
    print(f"Carbs/h: {plan.carbs_per_hour} g")
    print(f"Fluids/h: {plan.fluids_ml_per_hour} ml")
    print(f"Sodium/L: {plan.sodium_mg_per_l} mg")
    print(f"Formats: {', '.join(plan.recommended_formats)}")
    print(f"Risk: {plan.risk_level}")
    print("--- Packaging ---")
    print(f"Total fluids: {plan.total_fluids_ml} ml")
    print(f"Total carbs: {plan.total_carbs_g} g")
    print(f"Carrying capacity: {plan.carrying_capacity_ml} ml")
    print(f"Estimated bottles/flasks needed: {plan.estimated_bottles}")
    print(f"Estimated gels needed: {plan.estimated_gels}")
    print("Notes:")
    for note in plan.packaging_notes:
        print(f"- {note}")


if __name__ == "__main__":
    main()
