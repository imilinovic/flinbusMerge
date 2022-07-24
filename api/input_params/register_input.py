from pydantic.main import BaseModel


class RegisterInput(BaseModel):
    name: str
    surname: str
    email: str
    passwordHash: str
    username: str
