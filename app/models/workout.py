from datetime import date
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import validates

from app.extensions import db


class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date.today, nullable=False)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.Text)

    workout_exercises = db.relationship(
        "WorkoutExercise", back_populates="workout", cascade="all, delete-orphan"
    )

    __table_args__ = (
        CheckConstraint("duration_minutes > 0", name="ck_workout_duration_positive"),
    )

    @validates("date")
    def validate_date(self, key, value):
        if value and value > date.today():
            raise ValueError("Workout date cannot be in the future")
        return value

    def __repr__(self):
        return f"<Workout {self.date}>"
