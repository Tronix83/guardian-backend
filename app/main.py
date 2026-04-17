from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI()

# ✅ CORS (fixes browser blocking)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#  ROOT 
@app.get("/")
def root():
    return {"status": "Guardian backend alive"}

#  HEALTH CHECK
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/error")
def error():
    return{"status": "Error has ...."}


# SIMPLE WEBSOCKET
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("👻 WS CONNECTED 👻")
    
    while True:
        await websocket.send_json({
            "type": "test",
            "message": "WS working"
        })
        await asyncio.sleep(2)