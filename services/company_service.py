from db.db_deps_inj import get_db
from schema.company.company_request import CompanyRequest
from services.auth_service import check_valid_user
from exception.NotFoundException import NotFoundException
def create_company_service(company_request: CompanyRequest, email: str):
    db = get_db()
    user_id = check_valid_user(email)
    result = db.table("companies").insert({
        "name": company_request.name,
        "job_descriptions": company_request.job_descriptions,
        "userid": user_id
    }).execute()
    return result.data[0]
def get_list_company_service(email: str):
    db = get_db()
    user_id = check_valid_user(email)
    company_data = db.table("companies").select("*").eq("userid", user_id).execute()
    return company_data.data
def get_company_details_service(company_id: int):
    db = get_db()
    company_data = db.table("companies").select("*").eq("id", company_id).execute()
    if not company_data.data:
        raise NotFoundException(resource="company_details")
    return company_data.data[0]
def update_company_details_service(company_id: int, company_request: CompanyRequest):
    db = get_db()
    company_data = db.table("companies").update({"name": company_request.name, "job_descriptions": company_request.job_descriptions}).eq("id", company_id).execute()
    return company_data.data[0]
def delete_company_service(company_id: int):
    db = get_db()
    db.table("companies").delete().eq("id", company_id).execute()
    return