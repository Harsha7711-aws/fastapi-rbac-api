# FastAPI RBAC API

This project is a **FastAPI Backend API** with **JWT Authentication** and **Role-Based Access Control (RBAC)** using PostgreSQL as the database.

---

## 📦 Installation Steps

1. **Clone the Repository**
   [https://github.com/Harsha7711-aws/fastapi-rbac-api.git](https://github.com/Harsha7711-aws/fastapi-rbac-api.git)

```bash
git clone https://github.com/Harsha7711-aws/fastapi-rbac-api.git
cd fastapi-rbac-api
```

2. **Create Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Setup PostgreSQL Database**

* Ensure PostgreSQL is installed.
* Create a database named: `fastapi_rbac_db`
* Create a user: `fastapi_user` with password: `Harsha@123`
* Grant all privileges to the user on the database.

5. **Run the Application**

```bash
uvicorn app.main:app --reload
```

---

## ⚙️ API Endpoints

| Method | Endpoint  | Description                      |
| ------ | --------- | -------------------------------- |
| POST   | /register | Register new user (Admin/User)   |
| POST   | /login    | Obtain JWT token                 |
| GET    | /projects | Get all projects (Authenticated) |
| POST   | /projects | Create project (Admin Only)      |

---

## 📝 Usage Instructions

1. **Open Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. **Register a User** → `/register`
3. **Login with Credentials** → `/login` → Get JWT Token
4. **Click Authorize 🔒 in Swagger UI**, paste token as:

```bash
Bearer <your_access_token>
```

5. Access Protected Endpoints like `/projects`

---

## 📄 Dependencies

* FastAPI
* SQLModel
* psycopg2
* python-jose
* passlib
* python-dotenv
* python-multipart

---

## 📂 Folder Structure

```
fastapi-rbac-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── auth.py
│   └── dependencies.py
│
├── .env/
├── venv/
├── requirements.txt
└── README.md
```

---

## 🚀 Deployment (Optional)

* You can deploy on **Render**, **Heroku**, or any Cloud Platform with PostgreSQL support.

---

## 🔗 GitHub Repo

[https://github.com/Harsha7711-aws/fastapi-rbac-api](https://github.com/Harsha7711-aws/fastapi-rbac-api)
