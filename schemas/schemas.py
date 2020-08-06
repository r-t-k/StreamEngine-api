from typing import List, Optional
from pydantic import BaseModel
from datetime import date
from datetime import time
import uuid


class Base(BaseModel):
    id: int


class User(Base):
    status: str
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True



 
class Chat(Base):
    title : str
    #channel: Channel
    date: str
    class Config:
        orm_mode = True

class Channel(Base):
    title : str
    chats: List[Chat] = []
    class Config:
        orm_mode = True


class ChatMessage(Base):
    chat: Chat
    content: str
    user: User
    time: str
    class Config:
        orm_mode = True