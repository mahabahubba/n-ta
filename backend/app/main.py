from fastapi import FastAPI
from app.db.database import engine
from app.db import models


app = FastAPI(title="N-TA Backend")

# Creates the tables automatically based on the models defined in the models.py file.
# Runs when it starts up

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {"status": "ok"}
