from fastapi import APIRouter
from server.model.competition import Competition
from server.database import SessionLocal
from server.model.entry import Entry


count_entry = APIRouter()
db = SessionLocal()


# Get method to get the total number of entry of particular user
@count_entry.get('/total_competition/{id}')
def get_total_competition(id: int):

    get_total_competition = db.query(Competition.id).filter(Competition.user_id == id).all()
    total_competition = [ i['id'] for i in get_total_competition ]

    total = 0
    for com_id in total_competition:
        get_total_entry = db.query(Entry.id).filter(Entry.competition_id == com_id).all()
        total_entry = len([ j['id'] for j in get_total_entry])
        total += total_entry
    return total
