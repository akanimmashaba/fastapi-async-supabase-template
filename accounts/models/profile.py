from __future__ import annotations
from sqlmodel import SQLModel, Field
from uuid import UUID
from typing import Optional
from datetime import date


class Profile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    supabase_uid: UUID = Field(unique=True, index=True)
    name: str
    dob: date
    bio: Optional[str] = Field(default=None, max_length=500)
    height: Optional[float] = None
  