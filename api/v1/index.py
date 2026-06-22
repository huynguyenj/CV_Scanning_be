from fastapi import APIRouter
from api.v1.cv import router as cv_router
from api.v1.user import router as user_router
# Index include all others APIs
router = APIRouter(prefix='/api/v1')

# List APIs
router.include_router(cv_router)
router.include_router(user_router)