from fastapi import FastAPI
from db import *

app = FastAPI()




@app.get("/api/")
async def root():
    
    return {"message": channel_get_admin('test')}