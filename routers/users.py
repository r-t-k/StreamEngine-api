from typing import List
from fastapi import APIRouter, HTTPException
from db import *
from schemas import schemas


router = APIRouter()




#get one
@router.get("/{username}", response_model=schemas.User)
@db_session
def get_user(username: str):
    user = "no match found"

    if(username != None):
        user = User.get(username=username)


    return user


#get all
@router.get("/", response_model=List[schemas.User])
@db_session
def get_users():
    users = User.select_by_sql("SELECT * FROM user")

    return users

#create
@db_session
def user_create(username, email,password):
    User(username=username, email=email, password=password)

    user = User.get(username=username)
    return user.username + ' created'
   

#delete
@db_session
def user_delete(username = None, id = None):
    user = "no match found"

    if(username != None):
        user = User.get(username=username)
        user.delete()

    if(id != None):
        user = User.get(id=id)
        user.delete()

    return user.username + ' ID:' + str(user.id) + ' deleted'
