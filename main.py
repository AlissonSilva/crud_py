from fastapi import FastAPI
import view.user as user_view
from sqlalchemy import create_engine 
from util.util import Base, engine


Base.metadata.create_all(engine)
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(user_view.router)