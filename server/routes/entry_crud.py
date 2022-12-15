from fastapi import APIRouter, status
from server.schemas.entry import EntryDetails
from server.database import SessionLocal
from server.model.entry import Entry
from datetime import datetime


entryRouter = APIRouter()
db = SessionLocal()


@entryRouter.post("/entry", status_code=status.HTTP_201_CREATED)
def create_entry(entry: EntryDetails):
    """Post method to create new entry

    Args:
        entry (EntryDetails): _description_

    Returns:
        _type_: _description_
    """
    new_entry = Entry(
        title=entry.title,
        topic=entry.topic,
        state=entry.state,
        country=entry.country,
        competition_id=entry.competition_id,
    )
    db.add(new_entry)
    db.commit()
    return {"message": "Added successfully"}


@entryRouter.get("/entry", status_code=status.HTTP_200_OK)
def get_entry():
    """Get method to get the existing all the entry

    Returns:
        _type_: _description_
    """
    entry = db.query(Entry).all()
    return entry


@entryRouter.get("/entry/{id}", status_code=status.HTTP_200_OK)
def get_entry(id: int):
    """Get method to get the particular entry by id

    Args:
        id (int): _description_

    Returns:
        _type_: _description_
    """
    entry = db.get_entry(id).first()
    return entry


@entryRouter.put("/entry/{id}", status_code=status.HTTP_200_OK)
def update_entry(id: int, entry: EntryDetails):
    """Put method to update the exixting entry by id

    Args:
        id (int): _description_
        entry (EntryDetails): _description_

    Returns:
        _type_: _description_
    """
    entry_to_update = get_entry(id).first()
    entry_to_update.updated_at = datetime.now()
    entry_to_update.title = (entry.title,)
    entry_to_update.topic = (entry.topic,)
    entry_to_update.state = (entry.state,)
    entry_to_update.country = (entry.country,)
    entry_to_update.competition_id = entry.competition_id

    db.commit()
    return {"message": "entry updated successfully"}


@entryRouter.delete("/entry/{id}")
def delete_entry(id: int):
    """Delete method to delete a entry by id

    Args:
        id (int): _description_

    Returns:
        _type_: _description_
    """
    entry_to_delete = get_entry(id).first()
    db.delete(entry_to_delete)
    db.commit()

    return {"data": entry_to_delete, "message": "Ad delete successfully"}


def get_entry(id):

    return db.query(Entry).filter(Entry.id == id)
