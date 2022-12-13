from pydantic import BaseModel


class EntryDetails(BaseModel):
    title: str
    topic: str
    state: str
    country: str
    competition_id: int

    class Config:
        orm_mode = True
