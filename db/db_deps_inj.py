from supabase import Client
from db.db_connection import supabase_manager
def get_db() -> Client:
    return supabase_manager.client
