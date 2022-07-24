from typing import Optional

from pydantic.main import BaseModel


class RegisterResponse(BaseModel):
    success: bool
    apiKey: Optional[str]
