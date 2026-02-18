import { useEffect, useState } from "react";    

export const useNotifications = (token: string | null) => {
    const [notifications, setNotifications] = useState<string[]>([]);

    useEffect(() => {

        const ws = new WebSocket("ws://localhost:8000/ws/notifications");

        ws.onopen = () => {
            console.log("WebSocket connection established");
        };

        ws.onmessage = (event) => {
            console.log("Received notification:", event.data);
            setNotifications((prev) => [...prev, event.data]);
        };

        ws.onclose = () => {
            console.log("WebSocket connection closed");
        };
        
        ws.onerror = (error) => { 
            console.error("WebSocket error:", error);
        };

        return () => { 
            ws.close();
        };
    }   , []);

    return notifications; 

}