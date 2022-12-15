from pydantic import BaseModel


class EntryDetails(BaseModel):
    # id: int
    title: str
    topic: str
    state: str
    country: str
    competition_id: str

    class Config:
        orm_mode = True
