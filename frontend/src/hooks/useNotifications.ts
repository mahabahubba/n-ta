import { useEffect, useState } from "react";

interface Notification {
  id: number;
  message: string;
}

export const useNotifications = (token: string | null) => {
  const [notifications, setNotifications] = useState<Notification[]>([]);

  useEffect(() => {
    const ws = new WebSocket("ws://127.0.0.1:8000/ws/notifications");

    ws.onopen = () => console.log("WebSocket connection established");

    ws.onmessage = (event) => {
      const id = Date.now();
      const message = event.data;
      setNotifications((prev) => [...prev, { id, message }]);

      setTimeout(() => {
        setNotifications((prev) => prev.filter((n) => n.id !== id));
      }, 5000);
    };

    ws.onclose = () => console.log("WebSocket connection closed");
    ws.onerror = (error) => console.error("WebSocket error:", error);

    return () => ws.close();
  }, []);

  return notifications;
};