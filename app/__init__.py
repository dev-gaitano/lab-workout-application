from flask import Flask

from app.api import register_blueprints

from .config import Config
from .extensions import init_extensions, db, migrate


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    init_extensions(app)

    db.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)

    return app
