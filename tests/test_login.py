import requests

from api.input_params.register_input import RegisterInput


def run():
    payload = RegisterInput(
        name="Ivan",
        surname="Horvat",
        email="ivan.horvat@hrvatska.hr",
        passwordHash="notheuosnhausoneuhosanhue",
        username="ihorv",
    )
    res = requests.post("http://localhost:8000/api/register", json=payload.dict())
    print(res.json())
