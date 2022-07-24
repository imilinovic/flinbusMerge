from pydantic.main import BaseModel


class DBModel(BaseModel):

    @classmethod
    def get_field_names(cls, alias=False):
        return list(cls.schema(alias).get("properties").keys())
