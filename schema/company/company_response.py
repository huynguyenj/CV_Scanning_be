from pydantic import BaseModel

class CompanyResponse(BaseModel):
    id: int
    name: str
    job_descriptions: str
    userid: int

