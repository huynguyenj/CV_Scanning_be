from db.db_deps_inj import get_db
from exception.AppException import AppException
from exception.UnauthorizedException import UnauthorizedException
from schema.auth.auth_request import AuthRequest
def login_service(user_info: AuthRequest):
    db = get_db()
    is_email_exist = db.table("users")\
                      .select("email")\
                      .eq("email", user_info.email)\
                      .execute()
    if is_email_exist.data:
        return
    else:
        db.table("users").insert({"email": user_info.email, "name": user_info.name}).execute()
        return
def check_valid_user(user_email: str) :
    db = get_db()
    is_email_exist = db.table("users").select("email", "id").eq("email", user_email).execute()
    print("email: ",is_email_exist)
    if not is_email_exist.data:
        raise UnauthorizedException()
    else:
        return is_email_exist.data[0]["id"]