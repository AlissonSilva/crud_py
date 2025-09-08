from fastapi import FastAPI
import view.user as user_view, view.auth as auth_view
from sqlalchemy import create_engine 
from util.util import Base, engine


Base.metadata.create_all(engine)
app = FastAPI()

@app.get("/", tags=["Root"])
def read_root():
    return {"Server": "Online"}


app.include_router(auth_view.router)
app.include_router(user_view.router)