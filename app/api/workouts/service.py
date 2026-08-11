from datetime import date

from app.models import Workout, WorkoutExercise
from . import repository


def get_all_workouts():
    return repository.get_all_workouts()


def get_workout(workout_id):
    workout = repository.get_workout_by_id(workout_id)

    if workout is None:
        raise ValueError("Workout not found")

    return workout


def create_workout(data):
    workout_date = data.get("date")
    duration_minutes = data.get("duration_minutes")
    notes = data.get("notes")

    if workout_date:
        try:
            workout_date = date.fromisoformat(workout_date)
        except ValueError:
            raise ValueError("date must use YYYY-MM-DD format")
    else:
        workout_date = date.today()

    if workout_date > date.today():
        raise ValueError("Workout date cannot be in the future")

    if duration_minutes is not None:
        if (
            not isinstance(duration_minutes, int)
            or isinstance(duration_minutes, bool)
            or duration_minutes <= 0
        ):
            raise ValueError("duration_minutes must be a positive integer")

    workout = Workout(
        date=workout_date,
        duration_minutes=duration_minutes,
        notes=notes,
    )

    return repository.create_workout(workout)


def delete_workout(workout_id):
    workout = repository.get_workout_by_id(workout_id)

    if workout is None:
        raise ValueError("Workout not found")

    repository.delete_workout(workout)


def add_exercise_to_workout(workout_id, exercise_id, data):
    workout = repository.get_workout_by_id(workout_id)

    if workout is None:
        raise ValueError("Workout not found")

    exercise = repository.get_exercise_by_id(exercise_id)

    if exercise is None:
        raise ValueError("Exercise not found")

    reps = data.get("reps")
    sets = data.get("sets")
    duration_seconds = data.get("duration_seconds")

    if reps is None and sets is None and duration_seconds is None:
        raise ValueError("At least one of reps, sets, or duration_seconds is required")

    values = {
        "reps": reps,
        "sets": sets,
        "duration_seconds": duration_seconds,
    }

    for field, value in values.items():
        if value is not None:
            if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
                raise ValueError(f"{field} must be a positive integer")

    workout_exercise = WorkoutExercise(
        workout=workout,
        exercise=exercise,
        reps=reps,
        sets=sets,
        duration_seconds=duration_seconds,
    )

    return repository.add_exercise_to_workout(workout_exercise)
