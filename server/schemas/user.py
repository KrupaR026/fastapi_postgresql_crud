from pydantic import BaseModel


class UserCreation(BaseModel):
    # id: int
    name: str
    birth_date: str
    gender: str

    class Config:
        orm_mode = True
