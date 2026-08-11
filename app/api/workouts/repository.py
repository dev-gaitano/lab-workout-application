from app.extensions import db
from app.models import Exercise, Workout, WorkoutExercise


def get_all_workouts():
    return Workout.query.order_by(Workout.date.desc()).all()


def get_workout_by_id(workout_id):
    return db.session.get(Workout, workout_id)


def create_workout(workout):
    db.session.add(workout)
    db.session.commit()

    return workout


def delete_workout(workout):
    db.session.delete(workout)
    db.session.commit()


def get_exercise_by_id(exercise_id):
    return db.session.get(Exercise, exercise_id)


def add_exercise_to_workout(workout_exercise):
    db.session.add(workout_exercise)
    db.session.commit()

    return workout_exercise
