from pydantic import BaseModel, field_validator

class CompanyRequest(BaseModel):
    name: str
    job_descriptions: str

    @field_validator('name')
    @classmethod
    def validate_name(cls, v: str) -> str:
        if not v.strip(): # check if v is missing
            raise ValueError("Tên không được để trống")
        if len(v) > 100:
            raise ValueError("Tên không được quá 100 kí tự")
        return v.strip()
    @field_validator('job_descriptions')
    @classmethod
    def validate_job_descriptions(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Mô tả công việc không được để trống")
        return v.strip()
