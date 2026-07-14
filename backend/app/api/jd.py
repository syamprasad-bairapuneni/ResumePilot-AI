from fastapi import APIRouter
from pydantic import BaseModel

from app.services.jd_service import JDService

router = APIRouter()


class JDRequest(BaseModel):
    job_description: str


@router.post("/analyze")
async def analyze_jd(request: JDRequest):

    result = JDService.parse_jd(request.job_description)

    return {
        "success": True,
        "message": "Job Description parsed successfully.",
        "data": result
    }