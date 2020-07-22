from typing import List, Optional
from pydantic import BaseModel
from datetime import date
from datetime import time
import uuid





class UserBase(BaseModel):
    id : int
    username : str
    email : str
    password : str

class User(UserBase):
    id: int
    username : str
    email : str
    password : str
    class Config:
        orm_mode = True


