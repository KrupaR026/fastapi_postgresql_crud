from pydantic import BaseModel


class UserCreation(BaseModel):
    name: str
    birth_date: str
    gender: str

    class Config:
        orm_mode = True
