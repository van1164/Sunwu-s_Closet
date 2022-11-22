from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import s3bucket,recommend
from dotenv import load_dotenv
import os
app = FastAPI()
app.include_router(s3bucket.router)
app.include_router(recommend.router)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR,".env"))

origins = [
    "http://ec2-3-101-101-80.us-west-1.compute.amazonaws.com:8080",
    "http://ec2-3-101-101-80.us-west-1.compute.amazonaws.com",
    "http://ec2-3-101-101-80.us-west-1.compute.amazonaws.com:3000",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "test api"}
