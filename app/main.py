from fastapi import FastAPI
from sqlmodel import text

from app.core.database import SessionDep

app = FastAPI()


@app.get("/health")
async def db_health_check(db: SessionDep):
    query = text("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name = 'large_language_models'
        )
    """)
    result = await db.execute(query)
    table_exists = result.scalar()

    return {"table_exists": table_exists}