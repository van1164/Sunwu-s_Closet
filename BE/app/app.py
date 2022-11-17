from fastapi import FastAPI
from .routes import s3bucket
app = FastAPI()
app.include_router(s3bucket.router)

@app.get("/")
async def read_root():
    return {"message":"Test FastAPI"}