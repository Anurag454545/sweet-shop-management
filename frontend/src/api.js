import axios from "axios";

// Backend base URL
const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

// Attach JWT token to every request if available
API.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auth APIs
export const registerUser = (data) =>
  API.post("/api/auth/register", data);

export const loginUser = (data) =>
  API.post("/api/auth/login", data);

// Sweets APIs
export const getSweets = () =>
  API.get("/api/sweets");

export const searchSweets = (query) =>
  API.get(`/api/sweets/search?query=${query}`);

export const addSweet = (data) =>
  API.post("/api/sweets", data);

export const updateSweet = (id, data) =>
  API.put(`/api/sweets/${id}`, data);

export const deleteSweet = (id) =>
  API.delete(`/api/sweets/${id}`);

export const purchaseSweet = (id, quantity) =>
  API.post(`/api/sweets/${id}/purchase`, { quantity });

export const restockSweet = (id, quantity) =>
  API.post(`/api/sweets/${id}/restock`, { quantity });

export default API;
