from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from exception.AppException import AppException

def register_exception_handler(app: FastAPI):
    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        return JSONResponse(
            status_code=exc.status_code,
            content= {
                "status_code":exc.status_code,
                "message": exc.message,
                "code": exc.code,
            }
        )

# Ta dùng register_exception_handler để làm hàm wrapper
# Khi ở file application ta chỉ cần gọi hàm và truyền instance app vào là đc.
# Nếu ko dùng wrapper thì ta phải viết trực tiếp hàm app_exception_handler trong file application

# Nghĩa của hàm register_exception_handler : @app.exception_handler(AppException) =>
#   nói cho FastAPI bt khi nào có sự kiện raise mà liên quan tới AppException => gọi hàm app_exception_handler