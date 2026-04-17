from fastapi import WebSocket
import json

class WSManager:
    def __init__(self):
        self.clients = []

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.clients.append(ws)
        print("🟢 client connected")

    def disconnect(self, ws: WebSocket):
        if ws in self.clients:
            self.clients.remove(ws)
        print("🔴 client disconnected")

    async def broadcast(self, data: dict):
        dead = []

        for client in self.clients:
            try:
                await client.send_text(json.dumps(data))
            except:
                dead.append(client)

        for d in dead:
            self.disconnect(d)

manager = WSManager()