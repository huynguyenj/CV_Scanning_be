from fastapi import APIRouter, UploadFile, File

from schema.BaseResponse import BaseResponse
from schema.cv.ai_evaluation_response import AIEvaluationResponse
from schema.cv.cv_response import CvUploadResponse
from services.storage_service import upload_file_service
from services.ai_service import analysis_cv_service
router = APIRouter(prefix='/cv', tags=['CV api']) # tags use to define tag on Swagger

@router.post('/upload', response_model=BaseResponse[CvUploadResponse])
async def upload_file(file: UploadFile = File(...)):
    bytes_file = await file.read()
    file_name = file.filename
    file_path_response = upload_file_service(bytes_file, file_name)
    return BaseResponse(
        success= True,
        message= "Tải CV thành công",
        data= CvUploadResponse(
            file_path= file_path_response
        )
    )
@router.post('/upload/basic')
async def upload_basic(file: UploadFile = File(...)):
    bytes_file = await file.read()
    file_name = file.filename
    evaluation_response = analysis_cv_service(bytes_file)
    return BaseResponse(
        success= True,
        message= "Analysis success",
        data= AIEvaluationResponse(
            evaluation= evaluation_response
        )
    )

@router.get('/')
def get_list_cv():
    return {"messages": "List of cv"}
