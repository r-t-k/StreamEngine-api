from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from db import *
app = FastAPI()

class ChannelBase(BaseModel):
    title: str
    channel_meta: dict = None
   
#needs auth
#create 
@app.post("/api/channel/create")
async def create_channel(channel: ChannelBase):

    channel_create(channel.title)
    chan = channel_get(channel.title)

    return channel.title + ' created' + ' ID:' + str(chan.id)


#get
@app.get("/api/channel/{title}")
@db_session
async def get_channel(title: str):

    data = channel_get(title)

    return data.to_dict()