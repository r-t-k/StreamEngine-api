from typing import List
from fastapi import APIRouter, HTTPException
from db import *
from schemas import schemas
import datetime


router = APIRouter()




#get one
@router.get("/users/{username}", response_model=schemas.User)
@db_session
def get_user(username: str):
    user = "no match found"

    if(username != None):
        user = User.get(username=username)


    return user


#get all
@router.get("/users/", response_model=List[schemas.User])
@db_session
def get_users():
    users = User.select_by_sql("SELECT * FROM user")

    return users



#create
@router.post("/users/create", response_model=schemas.User)
@db_session
def create_user(username: str, password: str, email: str):
    user =  User(username=username, email=email, password=password, status= 'active')
    return user
   

### Channels

#get one
@router.get("/channels/{title}", response_model=schemas.Channel)
@db_session
def get_channel(title: str):
    channel = 'no match found' 

    if(title != None):
        channel = Channel.get(title=title)


    return channel


#get all
@router.get("/channels/", response_model=List[schemas.Channel])
@db_session
def get_channels():
    channels = Channel.select_by_sql("SELECT * FROM channel")

    return channels

#### Chat

@router.post("/chat/create", response_model=schemas.Chat)
@db_session
def create_chat(channel: int, date: str):
   
    chat =  Chat(channel = channel, date = date )

    return Chat

@router.post("/chat/msg/create", response_model=schemas.ChatMessage)
@db_session
def create_chatmsg(chat: int, content: str, user: int, time: str):
   
    msg =  ChatMessage(chat = chat, content=content, user=user, time=time )

    return ChatMessage