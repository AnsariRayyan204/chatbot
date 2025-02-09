from fastapi import APIRouter, UploadFile, File
import os
import fitz  # PyMuPDF

def extract_text_from_pdf(file_path: str) -> str:
    doc = fitz.open(file_path)
    text = ""
    
    for page in doc:
        text += page.get_text()  # Extract text from each page
    
    return text


router = APIRouter()


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure upload folder exists

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())
    # Extract text from PDF if the uploaded file is a PDF
    if file.filename.endswith('.pdf'):
        extracted_text = extract_text_from_pdf(file_location)
        return {"filename": file.filename, "status": "File uploaded successfully", "extracted_text": extracted_text[:500]}  # First 500 chars
    
    return {"filename": file.filename, "status": "File uploaded successfully"}




