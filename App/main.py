

from fastapi import FastAPI
from App.routes.upload import router as upload_router

app = FastAPI(
    title="AI KYC Verification System",
    version="1.0.0"
)

app.include_router(upload_router)