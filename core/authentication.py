from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError, ExpiredSignatureError
from config import get_settings
from fastapi import Depends
from exception.ExpiredTokenException import ExpiredTokenException
from exception.UnauthorizedException import UnauthorizedException
import requests
security = HTTPBearer()
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    # credentials: lấy Bearer token từ request ra và nó sẽ có cấu trúc object như sau:
    # "scheme": "Bearer",
    # "credentials": "gagahahhahahha" (token)
    settings = get_settings()

    # Bởi vì dùng login bằng google nên ta phải dùng phương thức đặc biệt để verify token
    # Gọi API của supabase để trả lại thông tin sign key cho chúng ta
    jwks = requests.get(settings.supabase_jwks_url).json()
    token = credentials.credentials
    try:
        payload = jwt.decode(
            token,
            # Secret key: đây là dạng key đặc biệt khi ta dùng login với platforms khác.
            jwks,
            algorithms=["RS256", "ES256"],
            # Cái này cần để validate token mà supabase đưa cho chúng ta
            issuer=settings.supabase_issuer,
            audience=settings.supabase_audience
        )
        return payload
    except ExpiredSignatureError:
        raise ExpiredTokenException()
    except JWTError:
        raise UnauthorizedException()
