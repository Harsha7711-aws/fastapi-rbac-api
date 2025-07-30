from sqlmodel import Session, select
from app import models, auth
from typing import Optional

# Register User
def create_user(session: Session, username: str, password: str, role: str):
    hashed_password = auth.get_password_hash(password)
    user = models.User(username=username, hashed_password=hashed_password, role=role)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# Authenticate User (for login)
def authenticate_user(session: Session, username: str, password: str) -> Optional[models.User]:
    statement = select(models.User).where(models.User.username == username)
    result = session.exec(statement).first()
    if result and auth.verify_password(password, result.hashed_password):
        return result
    return None

# Get User by Username
def get_user_by_username(session: Session, username: str) -> Optional[models.User]:
    statement = select(models.User).where(models.User.username == username)
    return session.exec(statement).first()

# Create Project
def create_project(session: Session, name: str, description: str):
    project = models.Project(name=name, description=description)
    session.add(project)
    session.commit()
    session.refresh(project)
    return project

# Get All Projects
def get_projects(session: Session):
    statement = select(models.Project)
    return session.exec(statement).all()
