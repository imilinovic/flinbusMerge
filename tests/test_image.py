import requests
import base64
from io import BytesIO
from PIL import Image

import settings
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
    res = requests.post(f"{settings.FLINBUSMERGE_URL}/api/register", json=payload.dict())

    if not res.json()['success']:
        print("Registering failed!")

    payload = LoginInput(
        username=username,
        passwordHash=passwordHash
    )
    res = requests.post(f"{settings.FLINBUSMERGE_URL}/api/login", json=payload.dict())

    token = res.json()['apiToken']
    data = requests.get('https://global.unitednations.entermediadb.net/assets/mediadb/services/module/asset/downloads/'
                        'preset/assets/2014/06/19456/image1170x530cropped.jpg').content

    image = Image.open(BytesIO(data))
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    image_b64 = base64.b64encode(buffered.getvalue())

    payload = ImageInput(
        apiToken=token,
        image=image_b64
    )
    res = requests.post(f"{settings.FLINBUSMERGE_URL}/api/image", json=payload.dict())

    print(res.json())
