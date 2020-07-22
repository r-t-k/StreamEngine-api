from fastapi import FastAPI
from db import *
from schemas import *
from routers import users

app = FastAPI()


app.include_router(users.router)
app.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

