from sqlalchemy import CheckConstraint
from sqlalchemy.orm import validates

from app.extensions import db


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False, nullable=False)

    workout_exercises = db.relationship("WorkoutExercise", back_populates="exercise")

    __table_args__ = (CheckConstraint("name != ''", name="ck_exercise_name_not_empty"),)

    @validates("name")
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Exercise name cannot be empty")
        return value.strip()

    @validates("category")
    def validate_category(self, key, value):
        allowed = {"strength", "cardio", "flexibility", "balance"}
        if value is None or value.lower() not in allowed:
            raise ValueError(f'Category must be one of: {", ".join(sorted(allowed))}')
        return value.lower()

    def __repr__(self):
        return f"<Exercise {self.name}>"
