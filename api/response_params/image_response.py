from typing import Optional

from pydantic.main import BaseModel


class ImageResponse(BaseModel):
    success: bool
    image: Optional[str]
