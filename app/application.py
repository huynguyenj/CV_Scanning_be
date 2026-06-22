from contextlib import asynccontextmanager

from fastapi import FastAPI
from db.db_connection import supabase_manager
from api.v1.index import router as index_v1
# Tự động chạy lifespan function khi ta khởi chạy server
@asynccontextmanager
async def lifespan (app: FastAPI):
    supabase_manager.connect()
    yield
    supabase_manager.disconnect()
app = FastAPI(lifespan=lifespan)
# lifespan là biến truyền vào để cho FastAPI bt khi bắt đầu chạy thì nó sẽ thực thi hay làm gì cùng thời điểm nó khởi chạy
# API V1
app.include_router(index_v1)

