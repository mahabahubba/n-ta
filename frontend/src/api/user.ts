const API_BASE = 'http://localhost:8000/api';

export async function fetchMe(token: string) {
    const res = await fetch(`${API_BASE}/me`, {
        headers: {
            Authorization: `Bearer ${token}`,
        },
    });
    if (!res.ok) {
        throw new Error('Failed to fetch user info');
    }
    return res.json();
}