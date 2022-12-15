from fastapi import APIRouter, status
from server.schemas.user import UserCreation
from server.database import SessionLocal
from server.model.user import User
from datetime import datetime


userRouter = APIRouter()
db = SessionLocal()


@userRouter.post("/user", status_code=status.HTTP_201_CREATED)
def create(user: UserCreation):
    """Post method to create new user

    Args:
        user (UserCreation): _description_

    Returns:
        _type_: _description_
    """
    new_user = User(
        name=user.name,
        birth_date=user.birth_date,
        gender=user.gender,
    )

    db.add(new_user)
    db.commit()
    return {"message": "User added successfully"}


@userRouter.get("/user", status_code=status.HTTP_200_OK)
def get_user():
    """Get method to get the existing all the user

    Returns:
        _type_: _description_
    """
    users = db.query(User).all()
    return users


@userRouter.get("/user/{id}", status_code=status.HTTP_200_OK)
def get_user_by_id(id: int):
    """Get method to get the particular user by id

    Args:
        id (int): _description_

    Returns:
        _type_: _description_
    """
    user = filter_users(id).first()
    return user


@userRouter.put("/user/{id}", status_code=status.HTTP_200_OK)
def update_user(id: int, user: UserCreation):
    """Put method to update the exixting user by id

    Args:
        id (int): _description_
        user (UserCreation): _description_

    Returns:
        _type_: _description_
    """
    user_to_update = filter_users(id).first()
    user_to_update.updated_at = datetime.now()
    user_to_update.name = (user.name,)
    user_to_update.birth_date = (user.birth_date,)
    user_to_update.gender = user.gender

    db.commit()
    return {"message": "User updated successfully"}


@userRouter.delete("/user/{id}")
def delete_user(id: int):
    """Delete method to delete a user by id

    Args:
        id (int): _description_

    Returns:
        _type_: _description_
    """
    user_to_delete = filter_users(id).first()
    db.delete(user_to_delete)
    db.commit()

    return {"data": user_to_delete, "message": "User delete successfully"}


def filter_users(id):

    return db.query(User).filter(User.id == id)
