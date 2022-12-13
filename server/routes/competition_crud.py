from fastapi import APIRouter, status
from server.schemas.competition import CompetitionDetails
from server.database import SessionLocal
from server.model.competition import Competition
from datetime import datetime


competitionRouter = APIRouter()
db = SessionLocal()


# Post method to create new competation
@competitionRouter.post('/competition', status_code=status.HTTP_201_CREATED)
def create(competition: CompetitionDetails):

    new_competition=Competition(
        name = competition.name,
        description = competition.description,
        user_id = competition.user_id,
    )

    db.add(new_competition)
    db.commit()
    return {"message": "Added successfully"}


# Get method to get the existing all the comtitions
@competitionRouter.get('/competition', status_code=status.HTTP_200_OK)
def get_competition():

    competitions = db.query(Competition).all()
    return competitions


# Get method to get the particular competition by id
@competitionRouter.get('/competition/{id}', status_code=status.HTTP_200_OK)
def get_competition(id: int):

    competition = db.query(Competition).filter(Competition.id == id).first()
    return competition


# Put method to update the exixting competition by id
@competitionRouter.put('/competition/{id}', status_code=status.HTTP_200_OK)
def update_competition(id: int, competition:CompetitionDetails):

    competition_to_update = db.query(Competition).filter(Competition.id == id).first()
    competition_to_update.updated_at = datetime.now()
    competition_to_update.name = competition.name,
    competition_to_update.description = competition.description
    competition_to_update.user_id = competition.user_id

    db.commit()
    return {"message": "competition updated successfully"}


# Delete method to delete a competition by id
@competitionRouter.delete('/competition/{id}')
def delete_competition(id: int):

    competition_to_delete = db.query(Competition).filter(Competition.id == id).first()
    db.delete(competition_to_delete)
    db.commit()

    return {"data": competition_to_delete, "message": "delete successfully"}
