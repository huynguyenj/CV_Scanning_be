import pdfplumber, io
from services.storage_service import download_file_service
def analysis_cv_basis_service(file: bytes):
    text = ""
    with pdfplumber.open(io.BytesIO(file)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
        # AI calling part in here:
        return text
def analysis_cv_advance_service(file_name: str):
    text = ""
    file_bytes = download_file_service(file_name=file_name)
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
        # AI calling part in here:
        return text