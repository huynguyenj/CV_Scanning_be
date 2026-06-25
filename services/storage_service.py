from db.db_connection import supabase_manager
from config import get_settings
from time import time

from exception.AppException import AppException
from random import randint

def upload_file_service(file: bytes, file_name: str):
    settings = get_settings()
    saving_file_name = f"{randint(1, 10000)}.pdf"
    try:
       response = supabase_manager.client.storage.from_(settings.supabase_bucket_name).upload(path=saving_file_name, file=file)
    except Exception as e:
        raise AppException(500, "ERROR", e)
    return response.path
