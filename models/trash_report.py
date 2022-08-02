from models.db_model import DBModel


class TrashReport(DBModel):
    reportPath: str
    reportId: str
    reportLongitude: float
    reportLatitude: float
    reportType: str
    profileUsername: str

    @classmethod
    def primary_key(cls) -> str:
        return "profileUsername"
