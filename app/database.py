import os
from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql+psycopg2://fastapi_user:Harsha%40123@localhost/fastapi_rbac_db"
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    import app.models
    SQLModel.metadata.create_all(engine)
