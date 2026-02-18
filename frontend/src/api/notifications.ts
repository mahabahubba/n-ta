export const fetchNotifications = async (token: string) => {
    const response = await fetch('http://localhost:8000/api/notifications', {
        headers: {
            Authorization: `Bearer ${token}`,
        },
    });
    if (!response.ok) {
        throw new Error('Failed to fetch notifications');
    }
    return response.json();
};
