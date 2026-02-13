from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.calls import Calls
from app.models.users import User
from app.schemas.calls import CallCreate

async def create_call_record(db: AsyncSession, call_in: CallCreate):
    query = select(User).where(User.phone_number == call_in.phone_number)
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    db_call = Calls(
        **call_in.model_dump(),
        user_id=user.id if user else None
    )

    # 3. Сохранение
    db.add(db_call)
    await db.commit()
    await db.refresh(db_call)
    return db_call

async def get_calls(db: AsyncSession, skip: int = 0, limit: int = 100):
    query = select(Calls).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()
