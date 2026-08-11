from sqlalchemy import CheckConstraint
from sqlalchemy.orm import validates

from app.extensions import db


class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"), nullable=False)
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    workout = db.relationship("Workout", back_populates="workout_exercises")
    exercise = db.relationship("Exercise", back_populates="workout_exercises")

    __table_args__ = (
        CheckConstraint(
            "(reps IS NULL OR reps > 0) AND (sets IS NULL OR sets > 0) AND (duration_seconds IS NULL OR duration_seconds > 0)",
            name="ck_workout_exercise_positive_values",
        ),
        CheckConstraint(
            "reps IS NOT NULL OR sets IS NOT NULL OR duration_seconds IS NOT NULL",
            name="ck_workout_exercise_has_data",
        ),
    )

    @validates("reps", "sets", "duration_seconds")
    def validate_positive(self, key, value):
        if value is not None and value <= 0:
            raise ValueError(f"{key} must be a positive number")
        return value

    def __repr__(self):
        return (
            f"<WorkoutExercise workout={self.workout_id} exercise={self.exercise_id}>"
        )
