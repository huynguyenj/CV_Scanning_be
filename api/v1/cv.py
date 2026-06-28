from fastapi import APIRouter, UploadFile, File
from fastapi.params import Depends
from schema.BaseResponse import BaseResponse
from schema.cv.ai_evaluation_response import AIEvaluationResponse
from schema.cv.cv_response import CvUploadResponse
from schema.user.user_data import UserInformation
from services.storage_service import upload_file_service
from services.ai_service import analysis_cv_basis_service, analysis_cv_advance_service
from core.authentication import get_current_user
from services.cv_service import create_cv_service
from services.evaluation_service import create_evaluation_service
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
            file_pdf_url= file_path_response
        )
    )
@router.post('/upload/basic')
async def upload_basic(file: UploadFile = File(...)):
    bytes_file = await file.read()
    file_name = file.filename
    evaluation_response = analysis_cv_basis_service(bytes_file)
    return BaseResponse(
        success= True,
        message= "Analysis success",
        data= AIEvaluationResponse(
            evaluation= evaluation_response
        )
    )
@router.post('/upload/cv/{company_id}', response_model=BaseResponse)
async def upload_cv_company(company_id: int, file: UploadFile = File(...), _: UserInformation = Depends(get_current_user)):
    bytes_file = await file.read()
    new_upload_file_name = upload_file_service(bytes_file, file.filename)
    cv_data = create_cv_service(company_id, new_upload_file_name)
    analysis_response = analysis_cv_advance_service(new_upload_file_name)
    create_evaluation_service(cv_data.id, analysis_response)
    return BaseResponse(
        success= True,
        message="Đánh giá cv hoàn tất",
        data= analysis_response
    )
@router.get('/')
def get_list_cv():
    return {"messages": "List of cv"}
