from models.profile import Profile
from utils.db_util import DBUtil

db = DBUtil()


def validate_token(api_token: str) -> bool:
    matches = db.filter(Profile, profileToken=api_token)

    return len(matches) == 1
