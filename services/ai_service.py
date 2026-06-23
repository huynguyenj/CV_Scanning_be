import pdfplumber, io
def analysis_cv_service(file: bytes):
    text = ""
    with pdfplumber.open(io.BytesIO(file)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
        # AI calling part in here:
        return text