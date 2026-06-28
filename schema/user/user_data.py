from typing import List
from pydantic import BaseModel, EmailStr, HttpUrl

class AppMetadata(BaseModel):
    provider: str
    providers: List[str]

class UserMetadata(BaseModel):
    avatar_url: HttpUrl
    email: str
    email_verified: bool
    full_name: str
    iss: HttpUrl
    name: str
    phone_verified: bool
    picture: HttpUrl
    provider_id: str
    sub: str

class AmrMethod(BaseModel):
    method: str
    timestamp: int

class UserInformation(BaseModel):
    iss: HttpUrl
    sub: str
    aud: str
    exp: int
    iat: int
    email: str
    phone: str
    app_metadata: AppMetadata
    user_metadata: UserMetadata
    role: str
    aal: str
    amr: List[AmrMethod]
    session_id: str
    is_anonymous: bool