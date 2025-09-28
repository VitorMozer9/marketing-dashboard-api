import jwt
import time
from typing import Dict
from src import config

def create_token(payload: Dict) -> str:
    now = int(time.time())
    data = payload.copy()
    data.update({"iat": now, "exp": now + config.JWT_EXP_SECONDS})
    token = jwt.encode(data, config.JWT_SECRET, algorithm=config.JWT_ALGORITHM)

    if isinstance(token, bytes):
        token = token.decode("utf-8")
    return token

def decode_token(token: str) -> Dict:
    return jwt.decode(token, config.JWT_SECRET, algorithms=[config.JWT_ALGORITHM])
