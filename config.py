# Simple version
# import os
# from dotenv import load_dotenv
# load_dotenv()
# supabase_key = os.getenv('supabase_key')

# Advance version
from anyio.functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Khai báo biến để Settings thừa kế BaseSettings sẽ biến class này thành validation
    # Với mỗi biến ta khai báo thì class Settings sẽ vào .env để đọc và dò nếu sai thì nó sẽ ngừng ứng dụng
    # supabase
    supabase_url: str
    supabase_publishable_key: str
    supabase_secret_key: str
    supabase_jwks_url: str
    supabase_bucket_name: str
    # chatgpt key
    open_ai_key: str


    model_config = SettingsConfigDict(
        env_file= ".env",
        env_file_encoding="utf-8",
        # ta dùng này do trong .env ta đặt tên biến viết hoa mà biến ta đặt trên viết thường
        case_sensitive=False,
        extra="ignore" # Bỏ qua TH các biến define mà ko sử dụng
    )

# @lru_cache() (Least Recently Used Cache) là một decorator dùng để lưu kết quả vào bộ nhớ đệm (RAM).
# Lần đầu tiên bạn gọi hàm get_settings(), Python sẽ vào file .env đọc dữ liệu, tạo ra object Settings và
# lưu object đó vào RAM.
# Từ lần gọi thứ 2 trở đi, hàm này sẽ trả về ngay lập tức object đã lưu trong RAM mà không cần đọc lại file .env nữa.
# all three of these return the exact same object in memory
# example:
# s1 = get_settings()
# s2 = get_settings()
# s3 = get_settings()

# print(s1 is s2 is s3)  # True (the same memory address)

@lru_cache()
def get_settings() -> Settings:
    return Settings()

