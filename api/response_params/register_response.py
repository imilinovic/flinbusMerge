from pydantic.main import BaseModel


class RegisterResponse(BaseModel):
    success: bool
