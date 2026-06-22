from supabase import Client
from db.db_connection import supabase_manager
# dependency injection
def get_db() -> Client:
    return supabase_manager.client
