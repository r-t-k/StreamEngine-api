from fastapi import APIRouter, HTTPException
from db import *
from schemas import schemas


router = APIRouter()




#get
@router.get("/{username}", response_model=schemas.User)
@db_session
def get_user(username: str):

    user = User.get(username=username)

    return user