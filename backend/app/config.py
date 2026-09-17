import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "development-only-change-me")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///wta.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

