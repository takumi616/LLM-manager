from fastapi import APIRouter, status

from app.crud import llm as crud
from app.core.database import SessionDep
from app.models.llms import LargeLanguageModelCreate, LargeLanguageModelPublic


router = APIRouter(prefix="/llms", tags=["llms"])

@router.post("", response_model=LargeLanguageModelPublic, status_code=status.HTTP_201_CREATED)
async def register_llm(session: SessionDep, llm: LargeLanguageModelCreate) -> LargeLanguageModelPublic:
    db_llm = await crud.register_llm(session, llm)
    return LargeLanguageModelPublic.model_validate(db_llm)