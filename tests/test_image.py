import requests
import base64
from io import BytesIO
from PIL import Image

from api.input_params.image_input import ImageInput
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
    res = requests.post("http://localhost:8000/api/register", json=payload.dict())

    if not res.json()['success']:
        print("Registering failed!")

    payload = LoginInput(
        username=username,
        passwordHash=passwordHash
    )
    res = requests.post("http://localhost:8000/api/login", json=payload.dict())

    token = res.json()['apiToken']
    data = requests.get('https://i.pinimg.com/736x/5b/94/d2/5b94d271031dcae72caf4ed5e60943f1.jpg').content

    image = Image.open(BytesIO(data))
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    image_b64 = base64.b64encode(buffered.getvalue())

    payload = ImageInput(
        apiToken=token,
        image=image_b64
    )
    res = requests.post("http://localhost:8000/api/image", json=payload.dict())

    print(res.json())
