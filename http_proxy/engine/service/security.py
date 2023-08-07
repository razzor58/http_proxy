import os
import random

from datetime import datetime

import jwt

SECRET_KEY = os.getenv("SECRET_KEY", "test")
NONCE_LENGTH = os.getenv("NONCE_LENGTH", 8)


def generate_nonce():
    return "".join([str(random.randint(0, 9)) for i in range(NONCE_LENGTH)])


def create_token() -> str:
    data = {
        "iat": int(datetime.now().timestamp()),
        "jti": generate_nonce(),
        "payload": {
            "user": "username",
            "date": datetime.now().date().strftime("%Y-%m-%d"),
        },
    }
    return jwt.encode(data, SECRET_KEY, algorithm="HS512")
