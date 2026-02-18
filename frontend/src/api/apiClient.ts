// axios allows for frontend http requests to be made to the backend
import axios from "axios";


// Create an instance with the base url of the backend
const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000',
});

export default apiClient;