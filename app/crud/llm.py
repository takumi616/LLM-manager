from sqlalchemy import select
from app.core.database import SessionDep
from app.models.llms import LargeLanguageModel, LargeLanguageModelCreate


async def register_llm(session: SessionDep, llm: LargeLanguageModelCreate) -> LargeLanguageModel:
    db_llm = LargeLanguageModel.model_validate(llm)
    session.add(db_llm)
    await session.commit()
    await session.refresh(db_llm)
    return db_llm


async def get_llm_by_id(session: SessionDep, id: str) -> LargeLanguageModel:
    stmt = select(LargeLanguageModel).where(LargeLanguageModel.id == id)
    result = await session.execute(stmt)
    db_llm = result.scalars().first()
    return db_llm