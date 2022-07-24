from pydantic.main import BaseModel


class ImageInput(BaseModel):
    apiToken: str
    image: str
