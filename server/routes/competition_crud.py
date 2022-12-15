from fastapi import APIRouter, status
from server.schemas.competition import CompetitionDetails
from server.database import SessionLocal
from server.model.competition import Competition
from datetime import datetime


competitionRouter = APIRouter()
db = SessionLocal()


@competitionRouter.post("/competition", status_code=status.HTTP_201_CREATED)
def create(competition: CompetitionDetails):
    """Post method to create new competation

    Args:
        competition (CompetitionDetails): _description_

    Returns:
        _type_: _description_
    """
    new_competition = Competition(
        name=competition.name,
        description=competition.description,
        user_id=competition.user_id,
    )

    db.add(new_competition)
    db.commit()
    return {"message": "Added successfully"}


@competitionRouter.get("/competition", status_code=status.HTTP_200_OK)
def get_competition():
    """Get method to get the existing all the comtitions

    Returns:
        _type_: _description_
    """
    competitions = db.query(Competition).all()
    return competitions


@competitionRouter.get("/competition/{id}", status_code=status.HTTP_200_OK)
def get_competition_by_id(id: int):
    """Get method to get the particular competition by id

    Args:
        id (int): _description_

    Returns:
        _type_: _description_
    """
    competition = filter_competitions(id).first()
    return competition


@competitionRouter.put("/competition/{id}", status_code=status.HTTP_200_OK)
def update_competition(id: int, competition: CompetitionDetails):
    """Put method to update the exixting competition by id

    Args:
        id (int): _description_
        competition (CompetitionDetails): _description_

    Returns:
        _type_: _description_
    """
    competition_to_update = filter_competitions(id).first()
    competition_to_update.updated_at = datetime.now()
    competition_to_update.name = (competition.name,)
    competition_to_update.description = competition.description
    competition_to_update.user_id = competition.user_id

    db.commit()
    return {"message": "competition updated successfully"}


@competitionRouter.delete("/competition/{id}")
def delete_competition(id: int):
    """Delete method to delete a competition by id

    Args:
        id (int): _description_

    Returns:
        _type_: _description_
    """
    competition_to_delete = filter_competitions(id).first()
    db.delete(competition_to_delete)
    db.commit()

    return {"data": competition_to_delete, "message": "delete successfully"}


def filter_competitions(id):

    return db.query(Competition).filter(Competition.id == id)
