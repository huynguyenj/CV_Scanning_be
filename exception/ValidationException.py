from exception.AppException import AppException

class ValidationException(AppException):
    def __init__(self, message: str = "Invalid input"):
        super().__init__(
            status_code=422,
            code="VALIDATION_ERROR",
            message=message
        )