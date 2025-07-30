from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from app.database import init_db, get_session
from app import schemas, crud, auth, dependencies

app = FastAPI()

# Initialize Database Tables
@app.on_event("startup")
def on_startup():
    init_db()

# User Registration Endpoint
@app.post("/register", response_model=schemas.Token)
def register(user_data: schemas.UserCreate, session: Session = Depends(get_session)):
    existing_user = crud.get_user_by_username(session, user_data.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    user = crud.create_user(session, user_data.username, user_data.password, user_data.role)
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# User Login Endpoint
@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = crud.authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Get All Projects (Any Authenticated User)
@app.get("/projects")
def read_projects(session: Session = Depends(get_session), current_user = Depends(dependencies.get_current_user)):
    projects = crud.get_projects(session)
    return projects

# Create Project (Admin Only)
@app.post("/projects")
def create_project(project: schemas.ProjectCreate, session: Session = Depends(get_session), current_admin = Depends(dependencies.get_current_admin_user)):
    new_project = crud.create_project(session, project.name, project.description)
    return new_project
