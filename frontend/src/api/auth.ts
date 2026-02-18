import apiClient from "./apiClient";


// Define the strucuture of the response that is received from the backend.
export interface AuthResponse {
    access_token: string;
    token_type: string;
}

// Makes POST request to the backend for new user registration and returns response data
export const registerUser = async (email: string, password: string) => {
    const response = await apiClient.post<AuthResponse>("/register", { email, password });
    return response.data;  
}

// Makes post request for login and return response data which includes access token which is used to authenticate in the backend.
// Needs to be in a json format to match the backend
export const loginUser = async (email: string, password: string) => {
    const response = await apiClient.post<AuthResponse>("/login", { email, password });
    return response.data;
};

