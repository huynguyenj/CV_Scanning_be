from contextlib import asynccontextmanager

from fastapi import FastAPI
from schema.test.request_test import TestRequest
from schema.test.response_test import TestResponse
import uuid
from db.db_connection import supabase_manager

# Tự động chạy lifespan function khi ta khởi chạy server
@asynccontextmanager
async def lifespan (app: FastAPI):
    supabase_manager.connect()
    yield
    supabase_manager.disconnect()
app = FastAPI(lifespan=lifespan)

posts = []

@app.get("/")
def index():
    return {"message": "Hello World"}
@app.post('/posts')
def post(post: TestRequest) -> TestResponse:
    new_post = { "id": str(uuid.uuid4()), "title": post.title, "content": post.content }
    posts.append(new_post)
    return new_post
