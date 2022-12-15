from pydantic import BaseModel


class CompetitionDetails(BaseModel):
    # id: int
    name: str
    description: str
    user_id: str

    class Config:
        orm_mode = True
