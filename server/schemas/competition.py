from pydantic import BaseModel


class CompetitionDetails(BaseModel):
    name: str
    description: str
    user_id: int

    class Config:
        orm_mode = True
