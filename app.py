import psycopg2
import requests
from flask import Flask, request

import settings
from api.input_params.image_input import ImageInput
from api.input_params.login_input import LoginInput
from api.input_params.register_input import RegisterInput
from api.response_params.image_response import ImageResponse
from api.response_params.login_response import LoginResponse
from api.response_params.register_response import RegisterResponse
from models.profile import Profile
from utils.db_util import DBUtil
from utils.random_util import gen_id
from utils.validation_util import validate_token

app = Flask(__name__)
db = DBUtil()


@app.route("/api/register", methods=["POST"])
def register():
    params = RegisterInput(**request.get_json())

    user_profile = Profile(
        profileUsername=params.username,
        profilePasswordHash=params.passwordHash,
        profileEmail=params.email,
        profileName=params.name,
        profileSurname=params.surname,
        profilePoints=0,
        profileTotalPoints=0,
        profileToken=gen_id(),
    )

    try:
        db.insert(user_profile)
    except psycopg2.errors.UniqueViolation:
        db.rollback()
        return RegisterResponse(success=False).dict()

    return RegisterResponse(success=True).dict()


@app.route("/api/login", methods=["POST"])
def login():
    params = LoginInput(**request.get_json())

    matches: list[Profile] = db.filter(Profile, profileUsername=params.username, profilePasswordHash=params.passwordHash)

    if len(matches) != 1:
        return LoginResponse(success=False).dict()

    user_profile = matches[0]
    user_profile.profileToken = gen_id()

    db.update(user_profile)

    return LoginResponse(success=True, apiToken=user_profile.profileToken).dict()


@app.route("/api/image", methods=["POST"])
def image():
    params = ImageInput(**request.get_json())

#    if not validate_token(params.apiToken):
#        return ImageResponse(success=False).dict()

    res = requests.post(settings.FLINBUSML_URL + '/yolo', json={"img": params.image})
    labeled_image = res.json()['img']

    return ImageResponse(success=True, image=labeled_image).dict()
