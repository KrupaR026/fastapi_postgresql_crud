from fastapi import APIRouter, status
from server.schemas.entry import EntryDetails
from server.database import SessionLocal
from server.model.entry import Entry
# from typing import List


entryRouter = APIRouter()
db = SessionLocal()


@entryRouter.post('/entry', status_code=status.HTTP_201_CREATED)
def create_entry(entry: EntryDetails):
    new_entry=Entry(
        # id=entry.id,
        title = entry.title,
        topic = entry.topic,
        state = entry.state,
        country = entry.country,
    )
    db.add(new_entry)
    db.commit()
    return {"message": "Added successfully"}


@entryRouter.get('/entry', status_code=status.HTTP_200_OK)
def get_entry():
    entry = db.query(Entry).all()
    return entry


@entryRouter.get('/entry/{id}', status_code=status.HTTP_200_OK)
def get_entry(id: int):
    entry = db.query(Entry).filter(Entry.id == id).first()
    return entry


@entryRouter.put('/entry/{id}', status_code=status.HTTP_200_OK)
def update_entry(id: int, entry:EntryDetails):
    entry_to_update = db.query(Entry).filter(Entry.id == id).first()
    # user_to_update.updated_at = datetime.datetime.now()
    # entry_to_update.id = entry.id,
    entry_to_update.title = entry.title,
    entry_to_update.topic = entry.topic,
    entry_to_update.state = entry.state,
    entry_to_update.country = entry.country,

    db.commit()
    return {"message": "entry updated successfully"}


@entryRouter.delete('/entry/{id}')
def delete_entry(id: int):
    entry_to_delete = db.query(Entry).filter(Entry.id == id).first()
    db.delete(entry_to_delete)
    db.commit()

    return {"data": entry_to_delete, "message": "Ad delete successfully"}