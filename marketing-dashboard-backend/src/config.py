import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET", "change_me")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXP_SECONDS = int(os.getenv("JWT_EXP_SECONDS", "3600"))

METRICS_CSV_PATH = os.getenv("METRICS_CSV_PATH", "./data/metrics.csv")
USERS_CSV_PATH = os.getenv("USERS_CSV_PATH", "./data/users.csv")
PORT = os.getenv("PORT", "5000")
