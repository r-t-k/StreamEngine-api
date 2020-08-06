from fastapi import FastAPI, WebSocket
from db import *
from schemas import *
from routers import users

app = FastAPI()



@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")



app.include_router(users.router)
app.include_router(
    users.router,
    prefix="",
    tags=[""],
    responses={404: {"description": "Not found"}},
)


@app.get("/test")
def root():
    t = channel_get(None, id=1)
    return {"message": t.title}