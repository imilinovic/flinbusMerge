from models.db_model import DBModel


class Profile(DBModel):
    profileUsername: str
    profilePasswordHash: str
    profilePoints: int
    profileEmail: str
    profileTotalPoints: int
    profileToken: str
    profileName: str
    profileSurname: str
