from fastapi import FastAPI

app = FastAPI(title="N-TA Backend")

@app.get("/")
def health_check():
    return {"status": "ok"}
