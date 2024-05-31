from typing import Optional
from pydantic import BaseModel, Field


class User(BaseModel):
    id: Optional[str] = Field(default_factory=str)
    name: str
    email: str
    password: str
    age: int
