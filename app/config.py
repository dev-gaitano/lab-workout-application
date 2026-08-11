from dotenv import load_dotenv

load_dotenv()


class Config:
    CORS_ORIGINS = []

    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
