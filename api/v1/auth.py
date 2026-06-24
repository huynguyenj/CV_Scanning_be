from fastapi import APIRouter

from schema.auth.auth_request import AuthRequest

router = APIRouter(prefix='/auth', tags=['auth'])

@router.post('/callback')
def login_callback(auth_request: AuthRequest):
    return {
        "name": auth_request.name,
        "email": auth_request.email,
    }