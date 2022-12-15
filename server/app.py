from fastapi import FastAPI
from server.routes.user_crud import userRouter
from server.routes.competition_crud import competitionRouter
from server.routes.entry_crud import entryRouter
from server.routes.count_entry_api import count_entry

app = FastAPI()


@app.get("/")
def home():
    """simple home page routes

    Returns:
        _type_: _description_
    """
    return {"data": "you are at the home page"}


app.include_router(userRouter, tags=["User"])
app.include_router(competitionRouter, tags=["Competition"])
app.include_router(entryRouter, tags=["Entry"])
app.include_router(count_entry, tags=["user_count_entry"])
