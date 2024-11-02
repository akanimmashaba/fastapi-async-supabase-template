# schemas/user_schemas.py
from pydantic import BaseModel
from uuid import UUID
from datetime import date

class CreateProfile(BaseModel):
    name: str
    dob: date
    bio: str

class ViewProfile(BaseModel):
    id: int
    supabase_uid: UUID
    name: str
    dob: date
    bio: str