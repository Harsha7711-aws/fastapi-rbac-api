# FastAPI RBAC API 🚀

This is a Backend API project built using **FastAPI**, **PostgreSQL**, and **JWT Authentication** with **Role-Based Access Control (RBAC)**.

---

## 📂 Features
- User Registration & Login
- JWT Token Authentication
- Role-based Project CRUD operations (Admin/User)
- PostgreSQL Database Integration
- Secure Password Hashing with Bcrypt

---

## ⚙️ Tech Stack
- FastAPI
- SQLModel (SQLAlchemy ORM)
- PostgreSQL
- JWT (via python-jose)
- Passlib (bcrypt)
- python-dotenv

---

## 🖥️ Installation Steps

### 1️⃣ Clone the Repository

git clone https://github.com/Harsha7711-aws/fastapi-rbac-api.git
cd fastapi-rbac-api

2️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
3️⃣ Install Dependencies

pip install -r requirements.txt
4️⃣ Setup PostgreSQL Database
Create a PostgreSQL Database named: fastapi_rbac_db

Create a user: fastapi_user with password: Harsha@123

Grant all privileges on database to that user.

5️⃣ Configure .env (Optional if hardcoded)
If you prefer using environment variables:



DATABASE_URL=postgresql+psycopg2://fastapi_user:Harsha@123@localhost/fastapi_rbac_db
SECRET_KEY=myverysecretkey
ACCESS_TOKEN_EXPIRE_MINUTES=30
▶️ Run the FastAPI Server

uvicorn app.main:app --reload
Visit Swagger UI at: http://127.0.0.1:8000/docs