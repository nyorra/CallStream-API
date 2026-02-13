from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.calls import CallCreate, CallResponce
from app.crud.calls import create_call_record
from app.api.deps import validate_token

router = APIRouter(tags=["Calls"])

@router.post("/", response_model=CallResponce, status_code=status.HTTP_201_CREATED)
async def create_call(
    call_in: CallCreate,
    db: AsyncSession = Depends(get_db),
    _service: str = Depends(validate_token)
):
    return await create_call_record(db=db, call_in=call_in)