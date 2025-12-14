🍬 Sweet Shop Management System

A full-stack Sweet Shop Management System built using FastAPI for the backend and React (Vite) for the frontend.
The application supports user authentication, JWT-based authorization, and CRUD operations for managing sweets.

🚀 Features
🔐 Authentication

User registration

User login

JWT-based authentication

Protected routes using Bearer tokens

🍩 Sweet Management

Add new sweets

View list of sweets

Search sweets by name

Update sweet details

Delete sweets

All sweet APIs are protected (auth required)

🧪 Testing

Backend APIs tested using pytest

Covers authentication and sweet management flows

🛠️ Tech Stack
Backend

FastAPI

SQLAlchemy

SQLite

JWT (python-jose)

Passlib (bcrypt)

Pytest

Frontend

React

Vite

Axios

CSS

📁 Project Structure
sweet-shop-management/
│
├── backend/
│   ├── app/
│   │   ├── auth.py
│   │   ├── database.py
│   │   ├── deps.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── main.py
│   │   └── routers/
│   │       ├── auth.py
│   │       └── sweets.py
│   ├── tests/
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
└── README.md

⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/Anurag454545/sweet-shop-management.git
cd sweet-shop-management

2️⃣ Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload


Backend will run at:

http://127.0.0.1:8000

3️⃣ Frontend Setup
cd frontend
npm install
npm run dev


Frontend will run at:

http://localhost:5173

🔑 API Endpoints
Authentication

POST /api/auth/register

POST /api/auth/login

Sweets (Protected)

GET /api/sweets

POST /api/sweets

PUT /api/sweets/{id}

DELETE /api/sweets/{id}

GET /api/sweets/search?query=

🧪 Running Tests
cd backend
pytest

📌 Notes

SQLite database is auto-created on backend startup

.db, venv, and node_modules are excluded via .gitignore

JWT token must be sent as:

Authorization: Bearer <token>

✅ Assignment Status

✔ Backend APIs implemented
✔ JWT Authentication
✔ Protected CRUD operations
✔ Frontend UI integrated
✔ Tests included
✔ GitHub repository ready

👤 Author

Anurag
Full-Stack Developer (FastAPI + React)
