from supabase import create_client, Client
from config import get_settings
settings = get_settings()
class SupabaseManager:
    def __init__(self):
        self._client: Client | None = None
    def connect(self):
        self._client = create_client(supabase_url=settings.supabase_url, supabase_key=settings.supabase_secret_key)
        print("Connected to Supabase")
    def disconnect(self):
        self._client = None
        print("Disconnected from Supabase")
    @property
    def client(self):
        if self._client is None:
            print("Supabase client not connected")
        return self._client

supabase_manager = SupabaseManager()
# Tạo instance trc khi gọi từ class khác thì chỉ cần import này vào
# Ko cần phải tạo mới instance mỗi lần import class SupabaseManager từ class khác => giảm bớt connection lại
# Phù hợp với singleton design
