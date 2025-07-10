from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings


DATABASE_URL = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@db:5432/{settings.POSTGRES_DB}"


engine: AsyncEngine = create_async_engine(
    DATABASE_URL,
    echo=True,  # Set to True for debugging purposes
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_= AsyncSession,
    expire_on_commit=False,
)

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session