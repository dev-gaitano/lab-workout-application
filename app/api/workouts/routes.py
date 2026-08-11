from flask import Blueprint, jsonify, request

from . import service

workout_bp = Blueprint( "workouts", __name__,)


def workout_to_dict(workout):
    return {
        "id": workout.id,
        "date": workout.date.isoformat(),
        "duration_minutes": workout.duration_minutes,
        "notes": workout.notes,
        "exercises": [
            {
                "id": workout_exercise.id,
                "exercise_id": workout_exercise.exercise_id,
                "exercise": {
                    "id": workout_exercise.exercise.id,
                    "name": workout_exercise.exercise.name,
                    "category": workout_exercise.exercise.category,
                    "equipment_needed": (workout_exercise.exercise.equipment_needed),
                },
                "reps": workout_exercise.reps,
                "sets": workout_exercise.sets,
                "duration_seconds": workout_exercise.duration_seconds,
            }
            for workout_exercise in workout.workout_exercises
        ],
    }


@workout_bp.get("")
def get_workouts():
    workouts = service.get_all_workouts()

    return jsonify([workout_to_dict(workout) for workout in workouts]), 200


@workout_bp.get("/<int:id>")
def get_workout(id):
    try:
        workout = service.get_workout(id)
    except ValueError as error:
        return jsonify({"error": str(error)}), 404

    return jsonify(workout_to_dict(workout)), 200


@workout_bp.post("")
def create_workout():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body is required"}), 400

    try:
        workout = service.create_workout(data)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    return jsonify(workout_to_dict(workout)), 201


@workout_bp.delete("/<int:id>")
def delete_workout(id):
    try:
        service.delete_workout(id)
    except ValueError as error:
        return jsonify({"error": str(error)}), 404

    return "", 204


@workout_bp.post("/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises")
def add_exercise_to_workout(workout_id, exercise_id):
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body is required"}), 400

    try:
        workout_exercise = service.add_exercise_to_workout(
            workout_id,
            exercise_id,
            data,
        )
    except ValueError as error:
        error_message = str(error)

        if error_message in {"Workout not found", "Exercise not found"}:
            return jsonify({"error": error_message}), 404

        return jsonify({"error": error_message}), 400

    return (
        jsonify(
            {
                "id": workout_exercise.id,
                "workout_id": workout_exercise.workout_id,
                "exercise_id": workout_exercise.exercise_id,
                "reps": workout_exercise.reps,
                "sets": workout_exercise.sets,
                "duration_seconds": workout_exercise.duration_seconds,
            }
        ),
        201,
    )
