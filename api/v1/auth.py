from fastapi import APIRouter
from fastapi.params import Depends

from core.authentication import get_current_user
from schema.BaseResponse import BaseResponse
from schema.auth.auth_request import AuthRequest
from services import auth_service
router = APIRouter(prefix='/auth', tags=['auth'])
@router.post('/callback', response_model=BaseResponse)
def login_callback(auth_request: AuthRequest):
    auth_service.login_service(auth_request)
    return BaseResponse(
        success=True,
        message="Login successful",
        data= None
    )