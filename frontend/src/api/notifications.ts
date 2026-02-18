export const connectNotfications = (token: string, onMessage: (message: string) => void) => {
    const ws = new WebSocket(`ws://127.0.0.1:8000/ws/notifications?token=${token}`);

    ws.onopen = () => {
        console.log("Connected to notifications server");
    };

    ws.onmessage = (event) => {
        onMessage(event.data);
    };

    ws.onclose = () => {
        console.log("Disconnected from notifications server");
    };

    ws.onerror = (error) => {
        console.error("WebSocket error:", error);
    };

    return ws;

}