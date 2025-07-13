from fastapi import APIRouter, status

from app.crud import llm as crud
from app.core.database import SessionDep
from app.models.llms import LargeLanguageModelCreate, LargeLanguageModelPublic, LargeLanguageModelUpdate


router = APIRouter(prefix="/llms", tags=["llms"])

@router.post("", response_model=LargeLanguageModelPublic, status_code=status.HTTP_201_CREATED)
async def register_llm(session: SessionDep, llm: LargeLanguageModelCreate) -> LargeLanguageModelPublic:
    db_llm = await crud.insert_llm(session, llm)
    return LargeLanguageModelPublic.model_validate(db_llm)


@router.get("", response_model=list[LargeLanguageModelPublic], status_code=status.HTTP_200_OK)
async def get_all_llms(session: SessionDep) -> list[LargeLanguageModelPublic]:
    db_llms = await crud.select_all_llms(session)
    return [LargeLanguageModelPublic.model_validate(db_llm) for db_llm in db_llms]


@router.get("/{id}", response_model=LargeLanguageModelPublic, status_code=status.HTTP_200_OK)
async def get_llm_by_id(session: SessionDep, id: str) -> LargeLanguageModelPublic:
    db_llm = await crud.select_llm_by_id(session, id)
    return LargeLanguageModelPublic.model_validate(db_llm)


@router.patch("/{id}", response_model=LargeLanguageModelPublic, status_code=status.HTTP_200_OK)
async def update_llm(session: SessionDep, id: str, llm: LargeLanguageModelUpdate) -> LargeLanguageModelPublic:
    db_llm = await crud.update_llm(session, id, llm)
    return LargeLanguageModelPublic.model_validate(db_llm)