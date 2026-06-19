from pydantic import BaseModel

class TestResponse(BaseModel):
    id: str
    title: str
    content: str