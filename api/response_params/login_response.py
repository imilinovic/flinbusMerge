from typing import Optional

from pydantic.main import BaseModel


class LoginResponse(BaseModel):
    success: bool
    apiToken: Optional[str]
