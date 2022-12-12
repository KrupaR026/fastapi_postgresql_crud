from pydantic import BaseModel
from typing import Optional


class UserCreation(BaseModel): 
    name: str
    birth_date: str
    gender: str

    class Config:
        orm_mode = True