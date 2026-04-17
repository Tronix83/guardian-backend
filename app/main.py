from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from app.soc.ws_manager import manager 
import random
import asyncio
from app.services.attacker_intel import analyze_ip


app = FastAPI()

# ✅ CORS (fixes browser blocking)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def soc_stream_simulator():
    while True:

        ip_pool = [
            "192.168.1.10",
            "10.0.0.5",
            "185.220.101.1",
            "45.155.205.233",
            "103.21.244.0"
        ]

        ip = random.choice(ip_pool)

        intel = analyze_ip(ip)

        event = {
            "type": "attacker_intel",
            "data": intel
        }

        await manager.broadcast(event)

        await asyncio.sleep(2)

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
    asyncio.create_task(soc_stream_simulator())


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