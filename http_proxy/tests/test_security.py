import os

from datetime import datetime

import jwt

from engine.service.security import create_token


def test_create_token():
    start_time = int(datetime.now().timestamp())
    token = create_token()
    secret_key = os.getenv("SECRET_KEY", "test")
    encoded_token = jwt.decode(token, secret_key, algorithms="HS512")

    assert encoded_token["payload"]["date"] == datetime.now().date().strftime(
        "%Y-%m-%d"
    )
    assert encoded_token["payload"]["user"] == "username"
    assert encoded_token["iat"] >= start_time
