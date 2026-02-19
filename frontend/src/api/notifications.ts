// This module provides functions to interact with the notifications API endpoint, allowing the frontend to fetch user notifications using an authentication token.
export const fetchNotifications = async (token: string) => {
  const response = await fetch(
    `${import.meta.env.VITE_API_BASE_URL}/notifications`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  if (!response.ok) {
    throw new Error("Failed to fetch notifications");
  }

  return response.json();
};
