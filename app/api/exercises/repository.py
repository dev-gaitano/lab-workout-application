from app.extensions import db
from app.models import Exercise, WorkoutExercise


def get_all_exercises():
    return Exercise.query.order_by(Exercise.name).all()


def get_exercise_by_id(exercise_id):
    return db.session.get(Exercise, exercise_id)


def create_exercise(exercise):
    db.session.add(exercise)
    db.session.commit()

    return exercise


def delete_workout_exercises(exercise):
    WorkoutExercise.query.filter_by(exercise_id=exercise.id).delete()


def delete_exercise(exercise):
    db.session.delete(exercise)
    db.session.commit()
