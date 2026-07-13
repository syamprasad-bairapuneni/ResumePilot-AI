from fastapi import APIRouter, UploadFile, File

from app.parser.resume_parser import ResumeParser
from app.services.resume_service import ResumeService

router = APIRouter()


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    # Read uploaded file
    contents = await file.read()

    # Validate file type
    if file.content_type != "application/pdf":
        return {
            "success": False,
            "message": "Only PDF files are supported."
        }

    # Extract text from PDF
    text = ResumeParser.extract_pdf_text(contents)

    # Extract structured information
    resume_data = ResumeService.parse_resume(text)

    return {
        "success": True,
        "message": "Resume parsed successfully.",
        "filename": file.filename,
        "data": resume_data,
        "text": text
    }