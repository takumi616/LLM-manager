from app.core.database import SessionDep
from app.models.llms import LargeLanguageModel, LargeLanguageModelCreate, LargeLanguageModelPublic


async def register_llm(session: SessionDep, llm: LargeLanguageModelCreate) -> LargeLanguageModelPublic:
    db_llm = LargeLanguageModel.model_validate(llm)
    print(db_llm)
    session.add(db_llm)
    await session.commit()
    await session.refresh(db_llm)
    return db_llm