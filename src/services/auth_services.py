from typing import Optional
from src.repositories.csv_repository import load_users_from_csv
from src.models.users import Users

class AuthService:
    def __init__(self, users_path: str = None):
        self._users = load_users_from_csv(users_path)

    def authenticate(self, email: str, password: str) -> Optional[Users]:
        email = email.strip().lower()
        for user in self._users:
            if user.email.lower() == email and user.password == password:
                return user
        return None

    def get_user_by_email(self, email: str) -> Optional[Users]:
        email = email.strip().lower()
        for u in self._users:
            if u.email.lower() == email:
                return u
        return None
