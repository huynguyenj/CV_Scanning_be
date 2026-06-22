from exception.AppException import AppException


class UnauthorizedException(AppException):
    def __init__(self):
        super().__init__(
            status_code=401,
            code="UNAUTHORIZED",
            message="Bạn không có quyền truy cập"
        )