from pydantic import BaseModel


class CompetitionDetails(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True