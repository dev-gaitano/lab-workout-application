from datetime import date, timedelta
from app import create_app
from app.extensions import db
from app.models import Workout, Exercise, WorkoutExercise

app = create_app()


def seed():
    app = create_app()

    with app.app_context():
        # Clear existing data in dependency order.
        db.session.query(WorkoutExercise).delete()
        db.session.query(Workout).delete()
        db.session.query(Exercise).delete()

        # Exercises
        exercises = [
            Exercise(
                name="Bench Press",
                category="strength",
                equipment_needed=True,
            ),
            Exercise(
                name="Squats",
                category="strength",
                equipment_needed=True,
            ),
            Exercise(
                name="Push Ups",
                category="strength",
                equipment_needed=False,
            ),
            Exercise(
                name="Running",
                category="cardio",
                equipment_needed=False,
            ),
            Exercise(
                name="Cycling",
                category="cardio",
                equipment_needed=True,
            ),
            Exercise(
                name="Plank",
                category="balance",
                equipment_needed=False,
            ),
            Exercise(
                name="Hamstring Stretch",
                category="flexibility",
                equipment_needed=False,
            ),
        ]

        db.session.add_all(exercises)
        db.session.flush()

        # Workouts
        today = date.today()

        workouts = [
            Workout(
                date=today - timedelta(days=6),
                duration_minutes=55,
                notes="Upper body strength workout",
            ),
            Workout(
                date=today - timedelta(days=4),
                duration_minutes=45,
                notes="Cardio and core session",
            ),
            Workout(
                date=today - timedelta(days=2),
                duration_minutes=60,
                notes="Lower body strength workout",
            ),
            Workout(
                date=today - timedelta(days=1),
                duration_minutes=35,
                notes="Light recovery session",
            ),
        ]

        db.session.add_all(workouts)
        db.session.flush()

        # Workout exercises
        workout_exercises = [
            # Upper body
            WorkoutExercise(
                workout=workouts[0],
                exercise=exercises[0],  # Bench Press
                reps=10,
                sets=4,
            ),
            WorkoutExercise(
                workout=workouts[0],
                exercise=exercises[2],  # Push Ups
                reps=15,
                sets=3,
            ),

            # Cardio + core
            WorkoutExercise(
                workout=workouts[1],
                exercise=exercises[3],  # Running
                duration_seconds=1800,
            ),
            WorkoutExercise(
                workout=workouts[1],
                exercise=exercises[5],  # Plank
                duration_seconds=180,
            ),

            # Lower body
            WorkoutExercise(
                workout=workouts[2],
                exercise=exercises[1],  # Squats
                reps=12,
                sets=4,
            ),
            WorkoutExercise(
                workout=workouts[2],
                exercise=exercises[4],  # Cycling
                duration_seconds=1200,
            ),

            # Recovery
            WorkoutExercise(
                workout=workouts[3],
                exercise=exercises[6],  # Hamstring Stretch
                duration_seconds=300,
            ),
            WorkoutExercise(
                workout=workouts[3],
                exercise=exercises[5],  # Plank
                duration_seconds=120,
            ),
        ]

        db.session.add_all(workout_exercises)

        db.session.commit()

        print("Database seeded successfully.")
        print(f"Exercises: {len(exercises)}")
        print(f"Workouts: {len(workouts)}")
        print(f"Workout exercises: {len(workout_exercises)}")


if __name__ == "__main__":
    seed()
