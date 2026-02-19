# N-TA
Nooriam Technical Assessment

A full stack-application that implements secure user authentication and real time-notification using modern backend and frontend technologies.

## Table of Contents
- [Tech Stack](#techstack)
- [Frontend](#frontend)
- [Backend](#backend)
- [Authentication](#authentication)
- [Database](#database)
- [Real-Time Notification](#real-time-notification)
- [Deployment](#deployment)
- [Testing](#completion-of-the-project-testing)
- [Getting Started](#getting-started)
- [Live Application](#live-application)


# TechStack
Frontend: React + TypeScript
Backend: FastAPI(Python)
Authentication: JWT (stateless)
Database: SQLite (via SQLAlchemy ORM)
Real-Time Notification: WebSockets
Deployment:
    BackEnd -> Railway
    FrontEnd -> Vercel


# FrontEnd
React and TypeScript was used in this project as it is an industry standard and allows for strong typing for API Responses. This can lead to more predictable component behaviours. Bootstrap was utilised due to the low complexity and its responsiveness to layout changes. Custom CSS was not used due to it being quite time-consuming.

# BackEnd
FastAPI designed for high performance and clean API design. FastAPI is an asynchronous Python web framework, which is ideal for concurrent users and in this case to utilise Websockets to provide that notification. There is also a built in API documentation (Swagger Doc). This in comparison to other frameworks:
- Flash: No Native async support and Websocket would require further extensions
- Django: Heavt framework for a task that only requires API-Only backend

Overall FastAPI would provide the best balance of performance and scalability for the current time being.

# Authentication
JWT is a stateless authenticaiton mechanisn where user identity is encoded into a signed token. Because it is stateless, there is no server side session storage and can scale horizontally. It is a widely adopted industry standard. In comparison to:
- Server Sessions: Harder to scale and is dependent on server memory
- Cookies only: CSRF concerns

# Database 
SQLAlchemu is a Python ORM that allows interaction with databases using Python objects instead of raw SQL. It integrates seamlessly with FastAPI, prevents SQL injection by default and improves maintianiability and readabaility. In comparison to:
- MongoDB: not ideal for relational authentication data
- Django ORM: tightly coupled with Django ORM

# Real-Time Notification
WebSockets provide persistant, bu-directional communciation between client and server. It provides real-time update and is supported by FastAPIs. In comparison to:
- HTTP Polling: Inefficient, high network overhead
- Long Polling: Complex and fragile
- Server-Sent Events: One directional only


# Deployment
- Railway
Railway provides a simple containerezed deployment, where it is Websocket compatiable. It also supports environement variable and automates HTTPS.

- Vercel
Vercel is optimized for React/Vite and is easy environment configuration.



# Completion of the project/ Testing
The approach I took to complete this project, was to keep testing and to build on top of the tested code before vamping up on any UI/UX changes.

I tested whether or not the data was going through the routes properly and adjusted accoridngly is there were any errors. I utilised Postman to test these routes and recieve any error.
[![Register]](./frontend/public/Register1.png)

Below depicts the postman route, if the email is already registered, for it to not accept it.
[![Email Exists]](./frontend/public/RegisterAlready.png)

When we utilise the email that has been registered for us to Login, which gives us an access token.
[![Login]](./frontend/public/Login.png)

To test whether this token returns the same user which is depicted by his id and email.
[![Corresponding]](./frontend/public/Corresponding.png)

Testing the Websocket to see whether we get a connection in the integrated terminal.
[![Websocket]](./frontend/public/WebSocketC.png)

Getting live notification of when a new user registers, it provides a notification to anyone active.
[![Notification]](./frontend/public/Notification.png)

For it to now work when it is deployed onto a live server:
[![Deployment]](./frontend/public/LiveServer.png)



## Getting Started

### Prerequisites
Make sure you have **Python** and **Node.js** installed before proceeding.

---

### Backend Setup

**1. Navigate to the backend directory and create a virtual environment**
```bash
cd backend
python -m venv venv
```

**2. Activate the virtual environment**
```bash
# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create a `.env` file in the `/backend` directory**
```env
SECRET_KEY=your_secret_key
```

**5. Start the backend server**
```bash
uvicorn app.main:app --reload
```

> Backend running at: `http://localhost:8000`

---

### Frontend Setup

**1. Navigate to the frontend directory and install dependencies**
```bash
cd ../frontend
npm install
```

**2. Create a `.env.local` file in the `/frontend` directory**
```env
VITE_API_BASE_URL=http://localhost:8000/api
VITE_WS_BASE_URL=ws://localhost:8000
```

**3. Start the development server**
```bash
npm run dev
```

> Frontend running at: `http://localhost:5173`


# Live Application
Please see link for the deployed application: https://n-ta.vercel.app/ 