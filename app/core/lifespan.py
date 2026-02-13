import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import engine, Base

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(_app: FastAPI):
    try:
        logger.info("🚀 Connecting to database and creating tables...")
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("✅ SQLAlchemy tables ensured.")
    except Exception as e:
        logger.error(f"❌ Database initialization failed: {e}")
        raise e

    yield

    await engine.dispose()
    logger.info("♻️ Database engine disposed.")
