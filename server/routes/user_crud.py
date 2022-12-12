from fastapi import APIRouter, status
from server.schemas.user import UserCreation
from server.database import SessionLocal
from server.model.user import User


userRouter = APIRouter()
db = SessionLocal()


@userRouter.post('/user', status_code=status.HTTP_201_CREATED)
def create(user: UserCreation):
    new_user=User(
        # id=user.id,
        name = user.name,
        birth_date = user.birth_date,
        gender = user.gender,
    )
    db.add(new_user)
    db.commit()
    return {"message": "User added successfully"}


@userRouter.get('/user', status_code=status.HTTP_200_OK)
def get_user():
    users = db.query(User).all()
    return users


@userRouter.get('/user/{id}', status_code=status.HTTP_200_OK)
def get_user(id: int):
    user = db.query(User).filter(User.id == id).first()
    return user


@userRouter.put('/user/{id}', status_code=status.HTTP_200_OK)
def update_user(id: int, user:UserCreation):
    user_to_update = db.query(User).filter(User.id == id).first()
    # user_to_update.updated_at = datetime.datetime.now()
    # user_to_update.id = user.id,
    user_to_update.name = user.name,
    user_to_update.birth_date = user.birth_date,
    user_to_update.gender = user.gender

    db.commit()
    return {"message": "User updated successfully"}


@userRouter.delete('/user/{id}')
def delete_user(id: int):
    user_to_delete = db.query(User).filter(User.id == id).first()
    db.delete(user_to_delete)
    db.commit()

    return {"data": user_to_delete, "message": "User delete successfully"}