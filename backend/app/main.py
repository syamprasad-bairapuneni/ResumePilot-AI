from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router as upload_router
from app.api.jd import router as jd_router

app = FastAPI(
    title="ResumePilot AI",
    description="AI-powered ATS Resume Builder",
    version="1.0.0"
)

# CORS Configuration
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Resume Routes
app.include_router(
    upload_router,
    prefix="/api",
    tags=["Resume"]
)

# Job Description Routes
app.include_router(
    jd_router,
    prefix="/api/jd",
    tags=["Job Description"]
)

# Root Endpoint
@app.get("/")
def root():
    return {
        "message": "ResumePilot AI Backend Running 🚀",
        "status": "success"
    }