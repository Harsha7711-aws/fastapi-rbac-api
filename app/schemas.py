from pydantic import BaseModel
from typing import Optional

# User Registration Request
class UserCreate(BaseModel):
    username: str
    password: str
    role: str  # 'admin' or 'user'

# User Login Request
class UserLogin(BaseModel):
    username: str
    password: str

# JWT Token Response
class Token(BaseModel):
    access_token: str
    token_type: str

# Project Create Request
class ProjectCreate(BaseModel):
    name: str
    description: str
