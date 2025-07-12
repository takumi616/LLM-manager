from fastapi import APIRouter

from app.api.routes import llms


api_router = APIRouter()
api_router.include_router(llms.router)