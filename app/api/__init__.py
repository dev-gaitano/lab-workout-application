from .workouts.routes import workout_bp
from .exercises.routes import exercise_bp


def register_blueprints(app):
    app.register_blueprints(
        workout_bp,
        url_prefix="/workouts",
    )
    app.register_blueprints(
        exercise_bp,
        url_prefix="/exercises",
    )
