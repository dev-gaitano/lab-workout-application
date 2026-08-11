from app.models import Exercise
from . import repository

ALLOWED_CATEGORIES = {
    "strength",
    "cardio",
    "flexibility",
    "balance",
}


def get_all_exercises():
    return repository.get_all_exercises()


def get_exercise(exercise_id):
    exercise = repository.get_exercise_by_id(exercise_id)

    if exercise is None:
        raise ValueError("Exercise not found")

    return exercise


def create_exercise(data):
    name = data.get("name")
    category = data.get("category")
    equipment_needed = data.get("equipment_needed", False)

    if not name or not name.strip():
        raise ValueError("Exercise name is required")

    if not category:
        raise ValueError("Exercise category is required")

    category = category.lower()

    if category not in ALLOWED_CATEGORIES:
        raise ValueError(
            "Category must be one of: " + ", ".join(sorted(ALLOWED_CATEGORIES))
        )

    if not isinstance(equipment_needed, bool):
        raise ValueError("equipment_needed must be a boolean")

    exercise = Exercise(
        name=name.strip(),
        category=category,
        equipment_needed=equipment_needed,
    )

    return repository.create_exercise(exercise)


def delete_exercise(exercise_id):
    exercise = repository.get_exercise_by_id(exercise_id)

    if exercise is None:
        raise ValueError("Exercise not found")

    # Stretch goal:
    # Remove the WorkoutExercise records that reference
    # this exercise before deleting the exercise itself.
    repository.delete_workout_exercises(exercise)

    repository.delete_exercise(exercise)
