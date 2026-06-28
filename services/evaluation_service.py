from db.db_deps_inj import get_db
import time
def create_evaluation_service(cv_id: str, response: str):
    db = get_db()
    evaluation_data = db.table("evaluations").insert({"cvid": cv_id, "response": response}).execute()
    return evaluation_data.data[0]