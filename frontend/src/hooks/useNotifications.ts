import { useEffect, useState } from "react";

interface Notification {
  id: number;
  message: string;
}

export const useNotifications = (token: string | null) => {
  const [notifications, setNotifications] = useState<Notification[]>([]);

  useEffect(() => {
    if (!token) return; // only connect if logged in

    const WS_BASE = import.meta.env.VITE_API_BASE_URL?.replace(/^http/, "ws");
    const ws = new WebSocket(`${WS_BASE}/ws/notifications`);

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
  }, [token]);

  return notifications;
};
