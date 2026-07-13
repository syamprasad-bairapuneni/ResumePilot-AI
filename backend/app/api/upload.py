from fastapi import APIRouter, UploadFile, File

from app.parser.resume_parser import ResumeParser

router = APIRouter()


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    contents = await file.read()

    if file.content_type != "application/pdf":
        return {
            "success": False,
            "message": "Only PDF files are supported."
        }

    text = ResumeParser.extract_pdf_text(contents)

    return {
        "success": True,
        "filename": file.filename,
        "text": text
    }