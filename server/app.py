from fastapi import FastAPI
from server.routes.user_crud import userRouter
from server.routes.competition_crud import competitionRouter
from server.routes.entry_crud import entryRouter

app = FastAPI()


@app.get('/')
def home():
    return {"data":"you are at the home page"}
    

app.include_router(userRouter, tags=["User"])
app.include_router(competitionRouter, tags=["Competition"])
app.include_router(entryRouter, tags=["Entry"])

