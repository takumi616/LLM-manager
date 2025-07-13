from fastapi import APIRouter, status

from app.crud import llm as crud
from app.core.database import SessionDep
from app.models.llms import LargeLanguageModelCreate, LargeLanguageModelPublic


router = APIRouter(prefix="/llms", tags=["llms"])

@router.post("", response_model=LargeLanguageModelPublic, status_code=status.HTTP_201_CREATED)
async def register_llm(session: SessionDep, llm: LargeLanguageModelCreate) -> LargeLanguageModelPublic:
    db_llm = await crud.insert_llm(session, llm)
    return LargeLanguageModelPublic.model_validate(db_llm)


@router.get("/{id}", response_model=LargeLanguageModelPublic, status_code=status.HTTP_200_OK)
async def get_llm_by_id(session: SessionDep, id: str) -> LargeLanguageModelPublic:
    db_llm = await crud.select_llm_by_id(session, id)
    return LargeLanguageModelPublic.model_validate(db_llm)