from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Shiksha backend!"}

@app.get("/healthz")
def health():
    return {"status": "ok"}
  
