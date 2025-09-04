from fastapi import FastAPI
import view.user as user_view

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(user_view.router)