// axios allows for frontend http requests to be made to the backend
import axios from "axios";


// Create an instance with the base url of the backend
const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});


export default apiClient;