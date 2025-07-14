from fastapi import HTTPException
from sqlalchemy import select
from app.core.database import SessionDep
from app.models.llms import LargeLanguageModel, LargeLanguageModelCreate, LargeLanguageModelMessage, LargeLanguageModelUpdate


async def insert_llm(session: SessionDep, llm: LargeLanguageModelCreate) -> LargeLanguageModel:
    db_llm = LargeLanguageModel.model_validate(llm)
    session.add(db_llm)
    await session.commit()
    await session.refresh(db_llm)
    return db_llm


async def select_all_llms(session: SessionDep) -> list[LargeLanguageModel]:
    result = await session.execute(select(LargeLanguageModel))
    db_llms = result.scalars().all()
    return db_llms


async def select_llm_by_id(session: SessionDep, id: str) -> LargeLanguageModel:
    stmt = select(LargeLanguageModel).where(LargeLanguageModel.id == id)
    result = await session.execute(stmt)
    db_llm = result.scalars().first()
    return db_llm


async def update_llm(session: SessionDep, id: str, llm: LargeLanguageModelUpdate) -> LargeLanguageModel:
    result = await session.execute(select(LargeLanguageModel).where(LargeLanguageModel.id == id))
    llm_db = result.scalars().first()
    if not llm_db:
        raise HTTPException(status_code=404, detail="LLM not found")
    
    llm_data = llm.model_dump(exclude_unset=True)
    llm_db.sqlmodel_update(llm_data)
    session.add(llm_db)
    await session.commit()
    await session.refresh(llm_db)
    return llm_db


async def delete_llm(session: SessionDep, id: str) -> LargeLanguageModelMessage:
    result = await session.execute(select(LargeLanguageModel).where(LargeLanguageModel.id == id))
    llm_db = result.scalars().first()
    if not llm_db:
        raise HTTPException(status_code=404, detail="LLM not found")
    
    await session.delete(llm_db)
    await session.commit()
    return LargeLanguageModelMessage(message="LLM deleted successfully")
