# APIRouter for handling WebSocket connections for notifications
# Websocket endpoint to send real-time notifications to clients
# WebsocketDisconnect to handle disconnections gracefully
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
# List to manage multiple active connections
from typing import List

router = APIRouter()

class ConnectionManager:
    # ConnectionManager class to manage active WebSocket connections and send notifications to clients
    def __init__(self):
        # Initialize an empty list to store active WebSocket connections
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        # Accept the incoming WebSocket connection and add it to the list of active connections
        await websocket.accept()
        self.active_connections.append(websocket)


    def disconnect(self, websocket: WebSocket):
        # Remove the WebSocket connection from the list of active connections when a client disconnects
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        # Send a message to all active WebSocket connections. It iterates through the list of active connections and sends the provided message to each connected client.
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@router.websocket("/ws/notifications")
async def websocket_endpoint(websocket: WebSocket):
    # WebSocket endpoint to handle incoming WebSocket connections for notifications. It uses the ConnectionManager to manage connections and broadcast messages.
    await manager.connect(websocket)
    try:
        while True:
            # Keep the connection open and wait for messages from the client (if needed)
            data = await websocket.receive_text()
            # For demonstration, we can broadcast received messages to all clients
            await websocket.send_text(f"Message received: {data}")
    except WebSocketDisconnect:
        # Handle disconnection gracefully by removing the WebSocket connection from the active connections list
        manager.disconnect(websocket)