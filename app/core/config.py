import os

class Settings:
    PROJECT_NAME = "Guardian SOC"
    ENV = os.getenv("ENV", "development")
    DEBUG = True

settings = Settings()