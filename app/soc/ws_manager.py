from fastapi import WebSocket
from typing import List
import json
import asyncio
import time

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        print("🟢 WS connected")

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
        print("🔴 WS disconnected")

    async def broadcast(self, message: dict):
        dead = []

        for conn in self.active_connections:
            try:
                await conn.send_text(json.dumps(message))
            except:
                dead.append(conn)

        for d in dead:
            self.disconnect(d)

manager = ConnectionManager()


# 🧪 SOC simulator (temporary feed)
async def soc_stream_simulator():
    while True:
        event = {
            "type": "scan",
            "timestamp": time.time(),
            "data": {
                "soc": {
                    "risk_score": 85,
                    "threat_level": "critical"
                },
                "learning": {
                    "ip": "10.0.0.1"
                },
                "analyst": {
                    "analysis": "Simulated SOC event active"
                }
            }
        }

        await manager.broadcast(event)
        await asyncio.sleep(2)