# asyncio and websockets are used to create a simple client connection to the WebSocket server and listen for incoming notifications.
import asyncio
import websockets

async def listen_notifications():
    url = "ws://127.0.0.1:8000/ws/notifications" 
    async with websockets.connect(url) as websocket:
        print("Connected to notifications server. Waiting for messages...")
        try:
            while True:
                message = await websocket.recv()
                print("New notification:", message)
        except websockets.ConnectionClosed:
            print("Connection closed")

if __name__ == "__main__":
    asyncio.run(listen_notifications())
