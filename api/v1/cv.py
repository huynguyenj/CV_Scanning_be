from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix='/cv', tags=['CV api']) # tags use to define tag on Swagger

# @router.post('/upload')
# async def upload_file(file: UploadFile = File(...)):
#     bytes_file = await file.read()
#     return { "data":  f"{bytes_file}"}
@router.get('/')
def get_list_cv():
    return {"messages": "List of cv"}
