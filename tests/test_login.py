import requests

import settings
from api.input_params.login_input import LoginInput
from api.input_params.register_input import RegisterInput


def run():
    username = "ihorv"
    passwordHash = "notheuosnhausoneuhosanhue"

    payload = RegisterInput(
        name="Ivan",
        surname="Horvat",
        email="ivan.horvat@hrvatska.hr",
        passwordHash=passwordHash,
        username=username,
    )
    res = requests.post(f"{settings.FLINBUSMERGE_URL}/api/register", json=payload.dict())

    if not res.json()['success']:
        print("Registering failed!")

    payload = LoginInput(
        username=username,
        passwordHash=passwordHash
    )
    res = requests.post(f"{settings.FLINBUSMERGE_URL}/api/login", json=payload.dict())

    print(res.json())
