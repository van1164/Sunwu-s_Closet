from fastapi import FastAPI
from .routes import s3bucket,recommend
from dotenv import load_dotenv
import os
app = FastAPI()
app.include_router(s3bucket.router)
app.include_router(recommend.router)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR,".env"))

@app.get("/")
async def main():
    return {"message": "test api"}
