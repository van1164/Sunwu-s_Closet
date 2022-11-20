from fastapi import FastAPI
from .routes import s3bucket
from dotenv import load_dotenv
import os
app = FastAPI()
app.include_router(s3bucket.router,prefix="/images")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR,".env"))

#아래 싹 다 라우팅하기
@app.get("/")
async def test():
    return {"test"}
@app.get("/app")
async def main():
    return {'User_content':[{'photo' : 'photoURL1', 'name' : 'photo_name_1', 'idx': '1'},
                            {'photo' : 'photoURL2', 'name' : 'photo_name_2', 'idx': '2'},
                            {'photo' : 'photoURL3', 'name' : 'photo_name_3', 'idx': '3'}]}
@app.get("/app/{idx}")
async def into_closet(idx : str):
    return {
        'prev_content' : {'photo:':'photo_url'+idx},
        'User_content':[{'photo' : 'photoURL1',  'idx': '1'},
                            {'photo' : 'photoURL2',  'idx': '2'},
                            {'photo' : 'photoURL3', 'idx': '3'}]}
    
@app.get("/app/recomandation/{idx}")
async def into_closet(idx : str):
    return {
        'User_content':{'photo' : 'photoURL'+idx,  'info_url': 'https://www.musinsa.com/app/blackfriday/special'}}