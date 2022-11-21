from fastapi import APIRouter
router = APIRouter()

@router.get("/app", tags=["into_closet"])
async def main_recommend():
    return {'User_content':[
        {'photo' : 'photoURL1', 'name' : 'photo_name_1', 'idx': '1'},
        {'photo' : 'photoURL2', 'name' : 'photo_name_2', 'idx': '2'},
        {'photo' : 'photoURL3', 'name' : 'photo_name_3', 'idx': '3'}]}

@router.get("/app/{idx}", tags=["into_closet_idx"])
async def into_closet(idx : str):
    return {
        'prev_content': {'photo:':'photo_url'+idx},
        'User_content':[
            {'photo' : 'photoURL1',  'idx': '1'},
            {'photo' : 'photoURL2',  'idx': '2'},
            {'photo' : 'photoURL3', 'idx': '3'}]}


@router.get("/app/recommendation/{idx}", tags=["recommendation_app"])
async def into_recommend_closet(idx : str):
    return {
        'User_content':
            {'photo': 'photoURL' + idx,
             'info_url': 'https://www.musinsa.com/app/blackfriday/special'}}