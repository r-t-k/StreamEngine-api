from fastapi import FastAPI
from db import *


app = FastAPI()

from channels import *



@app.get("/api/")
async def root():
    
    return {"message": user_create('admin', 'tom@kyser.dev', 'Scooby25')}