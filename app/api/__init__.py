from .workouts.routes import workout_bp


def register_blueprints(app):
    app.register_blueprints(
        workout_bp,
        url_prefix="/workouts",
    )
