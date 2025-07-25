from fastapi import FastAPI
from . import models, database
from .routes import auth

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Auth API is running!"}

