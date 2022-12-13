from fastapi import APIRouter, status
from server.schemas.entry import EntryDetails
from server.database import SessionLocal
from server.model.entry import Entry
from datetime import datetime


entryRouter = APIRouter()
db = SessionLocal()


# Post method to create new entry
@entryRouter.post('/entry', status_code=status.HTTP_201_CREATED)
def create_entry(entry: EntryDetails):

    new_entry=Entry(
        title = entry.title,
        topic = entry.topic,
        state = entry.state,
        country = entry.country,
        competition_id = entry.competition_id,
    )
    db.add(new_entry)
    db.commit()
    return {"message": "Added successfully"}


# Get method to get the existing all the entry
@entryRouter.get('/entry', status_code=status.HTTP_200_OK)
def get_entry():

    entry = db.query(Entry).all()
    return entry


# Get method to get the particular entry by id
@entryRouter.get('/entry/{id}', status_code=status.HTTP_200_OK)
def get_entry(id: int):

    entry = db.query(Entry).filter(Entry.id == id).first()
    return entry


# Put method to update the exixting entry by id
@entryRouter.put('/entry/{id}', status_code=status.HTTP_200_OK)
def update_entry(id: int, entry:EntryDetails):

    entry_to_update = db.query(Entry).filter(Entry.id == id).first()
    entry_to_update.updated_at = datetime.now()
    entry_to_update.title = entry.title,
    entry_to_update.topic = entry.topic,
    entry_to_update.state = entry.state,
    entry_to_update.country = entry.country,
    entry_to_update.competition_id = entry.competition_id

    db.commit()
    return {"message": "entry updated successfully"}


# Delete method to delete a entry by id
@entryRouter.delete('/entry/{id}')
def delete_entry(id: int):

    entry_to_delete = db.query(Entry).filter(Entry.id == id).first()
    db.delete(entry_to_delete)
    db.commit()

    return {"data": entry_to_delete, "message": "Ad delete successfully"}
