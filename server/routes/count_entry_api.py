from fastapi import APIRouter
from server.model.competition import Competition
from server.database import SessionLocal
from server.model.entry import Entry


count_entry = APIRouter()
db = SessionLocal()


@count_entry.get("/total_competition/{id}")
def get_total_competition(id: str):
    """Get method to get the total number of entry of particular user

    Args:
        id (int): _description_

    Returns:
        _type_: _description_
    """

    get_total_competition = (
        db.query(Competition.id).filter(Competition.user_id == id).all()
    )
    # get_total_competition = get_competitions(id).all()
    total_competition = [i["id"] for i in get_total_competition]

    total = 0
    for com_id in total_competition:
        get_total_entry = (
            db.query(Entry.id).filter(Entry.competition_id == com_id).all()
        )
        total_entry = len([j["id"] for j in get_total_entry])
        total += total_entry
    return total


# def get_competitions(id):

#     return db.query(Competition.id).filter(Competition.user_id == id)
