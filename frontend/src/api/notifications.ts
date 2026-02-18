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
