from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict
from typing import Literal

""" Базовая схема валидации входящих данный из json от сервиса типа ~Asterisk, все поля обязательны (...,)"""


class CallBase(BaseModel):
    call_id: str = Field(
        ...,
        min_length=32,
        max_length=32,
        examples=["a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"],
        description="ID звонка"
    )  # Уникальный номер для каждого звонка строго 32 символа

    phone_number: str = Field(
        ...,
        min_length=12,
        max_length=12,
        examples=["+79876543210"],
        description="Входящий номер"
    )  # Входящий номер

    call_type: Literal["incoming", "outgoing"] = Field(
        ...,
        description="Направление звонка",
        examples=["incoming"]
    )  # Звонок либо входящий, либо исходящий

    duration: int = Field(
        ...,
        gt=0,
        lt=3600,
        examples=[600],
        description="Длительность звонка (от 1с до 1ч)"
    )  # звонок в промежутке от 1 сек до 1 часа


""" То что мы ждем от сервиса, """


class CallCreate(CallBase):
    pass


""" То что мы отдаем клиенту """


class CallResponce(CallBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
