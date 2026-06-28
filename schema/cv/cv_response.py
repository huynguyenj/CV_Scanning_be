from pydantic import BaseModel

class CvUploadResponse(BaseModel):
    id: int
    file_pdf_url: str
    companyid: int