from exception.AppException import AppException
class ExpiredTokenException(AppException):
    def __init__(self):
        super().__init__(
            status_code=401,
            code='TOKEN_EXPIRED',
            message="Phiên làm việc của bạn đã hết hạn. Hãy đăng nhập lại"
        )
