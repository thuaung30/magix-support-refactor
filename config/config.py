from dotenv import load_dotenv
import os

env_path = os.path.join(os.getcwd(), '.env')
load_dotenv(dotenv_path=env_path)

print(env_path)

class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME") or "Magix Support"
    PROJECT_VERSION: str = os.getenv("PROJECT_VERSION") or "0.0.1"

    DATABASE_URL: str = os.getenv("DATABASE_URL") or "postgresql://postgres:postgres@localhost:5432/magixsupport"
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

settings = Settings()
