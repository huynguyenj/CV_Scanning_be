from db.db_deps_inj import get_db
from schema.cv.cv_response import CvUploadResponse
def create_cv_service(company_id: int, file_cv_url: str):
    db = get_db()
    cv_data = db.table("cv").insert({"file_pdf_url": file_cv_url, "companyid": company_id}).execute()
    return CvUploadResponse(**cv_data.data[0])
def get_list_cv_service(company_id: int):
    db = get_db()
    list_cv_data = db.table("cv").select("*").eq({"companyid": company_id}).execute()
    return list_cv_data.data
def delete_cv_service(cv_id: int):
    db = get_db()
    db.table("cv").delete().eq("id", cv_id)
    return