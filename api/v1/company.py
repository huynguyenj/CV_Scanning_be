from fastapi import APIRouter
from fastapi.params import Depends
from core.authentication import get_current_user
from schema.BaseResponse import BaseResponse
from schema.company.company_request import CompanyRequest
from schema.company.company_response import CompanyResponse
from schema.user.user_data import UserInformation
from services.company_service import create_company_service, get_list_company_service, get_company_details_service, update_company_details_service, delete_company_service
from typing import List
router = APIRouter(prefix='/company', tags=['Company'])

@router.post("/creation", response_model=BaseResponse[CompanyResponse])
def create_company(company_info: CompanyRequest, current_user: UserInformation = Depends(get_current_user)):
    company_data = create_company_service(company_info, current_user.user_metadata.email)
    return BaseResponse(
        success=True,
        message="Tạo công ty thành công",
        data=company_data
    )
@router.get("/list", response_model=BaseResponse[List[CompanyResponse]])
def get_list_companies(current_user: UserInformation = Depends(get_current_user)):
    list_companies = get_list_company_service(current_user.email)
    return BaseResponse(
        success= True,
        message="Lấy danh sách công ty thành công",
        data=list_companies
    )
@router.get("/{company_id}", response_model=BaseResponse)
def get_company_details(company_id: int, _: UserInformation = Depends(get_current_user)):
    company_data = get_company_details_service(company_id)
    return BaseResponse(
        success=True,
        message="Lấy thông tin công ty thành công",
        data=company_data
    )
@router.put("/{company_id}", response_model=BaseResponse)
def update_company_details(company_id: int, company_data: CompanyRequest):
    company_data = update_company_details_service(company_id, company_data)
    return BaseResponse(
        success=True,
        message="Cập nhật thành công",
        data = company_data
    )
@router.delete("/{company_id}", response_model=BaseResponse)
def delete_company(company_id: int):
    delete_company_service(company_id)
    return BaseResponse(
        success=True,
        message="Xóa thành công",
        data= None
    )