from datetime import date

from app.extensions import db


class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date.today, nullable=False)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.Text)

    exercises = db.relationship(
        "WorkoutExercise", back_populates="workout", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Workout {self.date}>"
