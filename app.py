import psycopg2
from flask import Flask, request

from api.input_params.register_input import RegisterInput
from api.response_params.register_response import RegisterResponse
from db_util import DBUtil
from models.profile import Profile
from random_util import gen_id

app = Flask(__name__)
db = DBUtil()


@app.route("/api/register", methods=["GET", "POST"])
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
        profileToken=gen_id()
    )

    try:
        db.insert(user_profile)
    except psycopg2.errors.UniqueViolation:
        db.rollback()
        return RegisterResponse(success=False).dict()

    return RegisterResponse(success=True, apiKey=user_profile.profileToken).dict()
