from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from app.soc.ws_manager import manager 
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

@app.on_event("startup")
async def startup():
    async def fake_feed():
        while True:
            await manager.broadcast({
                "type": "soc_event",
                "risk": 90,
                "message": "simulated intrusion"
            })
            await asyncio.sleep(2)

    asyncio.create_task(fake_feed())


# SIMPLE WEBSOCKET
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    print("👻 WS CONNECTED 👻")
    
    try:
        while True:
            await websocket.receive_text()
    except:
        manager.disconnect(websocket)