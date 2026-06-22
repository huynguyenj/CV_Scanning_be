from exception.AppException import AppException

class NotFoundException(AppException):
    def __init__(self, resource: str = "Resource"):
        super().__init__(
            status_code=404,
            code="NOT_FOUND",
            message=f"{resource} not found"
        )
