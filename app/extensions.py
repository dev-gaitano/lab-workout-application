from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

cors = CORS()

db = SQLAlchemy()


def init_extensions(app):
    cors.init_app(
        app,
        resources={
            r"/api/*": {
                "origins": app.config["CORS_ORIGINS"],
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization"],
                "supports_credentials": True,
            }
        },
    )
