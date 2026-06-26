from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from core.origin_constant import ORIGINS
from db.db_connection import supabase_manager
from api.v1.index import router as index_v1
from core.exception_handler import register_exception_handler
from fastapi.middleware.cors import CORSMiddleware
# Tự động chạy lifespan function khi ta khởi chạy server
@asynccontextmanager
async def lifespan (app: FastAPI):
    supabase_manager.connect()
    yield
    supabase_manager.disconnect()
app = FastAPI(lifespan=lifespan, swagger_ui_parameters={"persistAuthorization": True})
# lifespan là biến truyền vào để cho FastAPI bt khi bắt đầu chạy thì nó sẽ thực thi hay làm gì cùng thời điểm nó khởi chạy
# Register exception handler
app.add_middleware(
    CORSMiddleware,
    allow_origins= ORIGINS,
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"],
)
register_exception_handler(app)
# API V1
app.include_router(index_v1)
# Customer openapi
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="CV Scanner API",
        version="1.0.0",
        routes=app.routes,
    )
    # add Bearer security scheme
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    # apply globally to all routes
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema
app.openapi = custom_openapi

