from pydantic.main import BaseModel


class LoginInput(BaseModel):
    username: str
    passwordHash: str
