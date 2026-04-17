from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from app.soc.ws_manager import manager 
import random
import asyncio
from app.services.attacker_intel import analyze_ip
from app.ai.soc_analyst import analyze_event


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

        intel = analyze_ip(ip)  

        event = {
            "type": "attacker_intel",
            "data": intel
        }

        ai_analysis = analyze_event(intel)

        event["ai"] = ai_analysis

        print("SOC EVENT SENT:", event)

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