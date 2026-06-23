from pydantic import BaseModel

class CvUploadResponse(BaseModel):
    file_path: str