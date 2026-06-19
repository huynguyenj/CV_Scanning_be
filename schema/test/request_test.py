from pydantic import BaseModel

class TestRequest(BaseModel):
    title: str
    content: str