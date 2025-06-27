# 🔐 FastAPI Auth Service

A secure authentication API built with **FastAPI**, demonstrating user registration and login using **JWT**, **Pydantic**, and **SQLAlchemy**. The project is containerized with **Docker** and supports local development and deployment.

---

## 🚀 Features

- ✅ User registration with hashed passwords  
- 🔑 JWT-based login authentication  
- 🧩 Modular architecture (routers, models, schemas)  
- 📦 Docker & Docker Compose for easy setup  
- 🧪 Swagger UI auto-generated  
- 🔒 Token-based security logic  

---

## 🧰 Tech Stack

- **Python 3.10**
- **FastAPI**
- **SQLAlchemy**
- **PyJWT**
- **Pydantic**
- **Docker / Docker Compose**

---

## 📁 Project Structure

```
fastapi-auth-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routes/
│       ├── __init__.py
│       └── auth.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🐳 Running Locally with Docker

Make sure Docker and Docker Compose are installed, then run:

```bash
docker-compose up --build
```

Then open your browser at:

- http://localhost:8000/docs 👉 Swagger UI  
- http://localhost:8000 👉 Health check  

---

## 🔗 API Endpoints

| Description         | Path       | Method |
|---------------------|------------|--------|
| Register new user   | `/register`| POST   |
| Login and get JWT   | `/login`   | POST   |
| Health check        | `/`        | GET    |

---

## 🔐 Authentication

After login, you'll receive a JWT token which should be passed as:

```
Authorization: Bearer <your_token_here>
```

---

## 🧪 Example Login Request

```bash
curl -X POST http://localhost:8000/login \
 -H "Content-Type: application/json" \
 -d '{
   "email": "user@example.com",
   "password": "your_password"
 }'
```

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## ✨ Author

Developed by **afshin-8**  
Check out my other DevOps and FastAPI projects 🚀

