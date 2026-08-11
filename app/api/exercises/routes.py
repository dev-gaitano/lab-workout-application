from flask import Blueprint, jsonify, request

from . import service

exercise_bp = Blueprint(
    "exercises",
    __name__,
)


def exercise_to_dict(exercise):
    return {
        "id": exercise.id,
        "name": exercise.name,
        "category": exercise.category,
        "equipment_needed": exercise.equipment_needed,
    }


def exercise_detail_to_dict(exercise):
    return {
        "id": exercise.id,
        "name": exercise.name,
        "category": exercise.category,
        "equipment_needed": exercise.equipment_needed,
        "workouts": [
            {
                "id": workout_exercise.workout.id,
                "date": workout_exercise.workout.date.isoformat(),
                "duration_minutes": (workout_exercise.workout.duration_minutes),
                "notes": workout_exercise.workout.notes,
                "reps": workout_exercise.reps,
                "sets": workout_exercise.sets,
                "duration_seconds": workout_exercise.duration_seconds,
            }
            for workout_exercise in exercise.workout_exercises
        ],
    }


@exercise_bp.get("")
def get_exercises():
    exercises = service.get_all_exercises()

    return jsonify([exercise_to_dict(exercise) for exercise in exercises]), 200


@exercise_bp.get("/<int:id>")
def get_exercise(id):
    try:
        exercise = service.get_exercise(id)
    except ValueError as error:
        return jsonify({"error": str(error)}), 404

    return jsonify(exercise_detail_to_dict(exercise)), 200


@exercise_bp.post("")
def create_exercise():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body is required"}), 400

    try:
        exercise = service.create_exercise(data)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    return jsonify(exercise_to_dict(exercise)), 201


@exercise_bp.delete("/<int:id>")
def delete_exercise(id):
    try:
        service.delete_exercise(id)
    except ValueError as error:
        return jsonify({"error": str(error)}), 404

    return "", 204
