// This module provides functions to interact with the user-related API endpoints, allowing the frontend to fetch user information using an authentication token.
const API_BASE = `${import.meta.env.VITE_API_BASE_URL}`;

export async function fetchMe(token: string) {
  const res = await fetch(`${API_BASE}/me`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!res.ok) {
    throw new Error("Failed to fetch user info");
  }

  return res.json();
}
