from fastapi import APIRouter
from ..__init__ import result_style,result_cody_detail,result_item_detail_new,le2,le
from .recom2 import Recomand
router = APIRouter()

@router.get("/app", tags=["into_closet"])
async def main_recommend():
    return {'User_content':[
        {'photo' : 'https://github.com/van1164/Sunwu-s_Closet/blob/main/img/KakaoTalk_20221113_145639673.jpg?raw=true', 'name' : '편하게', 'idx': '1'},
        {'photo' : 'https://github.com/van1164/Sunwu-s_Closet/blob/main/img/KakaoTalk_20221113_170527576.jpg?raw=true', 'name' : '아끼는 옷', 'idx': '2'},
        {'photo' : 'https://github.com/van1164/Sunwu-s_Closet/blob/main/img/KakaoTalk_20221113_161928184.jpg?raw=true', 'name' : '누나 만날때 입을 옷', 'idx': '3'}]}
    
    

@router.get("/app/{idx}", tags=["into_closet_idx"])
async def into_closet(idx : str):

    if idx =='1':
        lst = Recomand(result_item_detail_new,result_cody_detail,result_style,['상의','navy'],le2,le)
        photo_url ='https://github.com/van1164/Sunwu-s_Closet/blob/main/img/KakaoTalk_20221113_145639673.jpg?raw=true'
    elif idx =='2':
        lst = Recomand(result_item_detail_new,result_cody_detail,result_style,['상의','grey'],le2,le)
        photo_url ='https://github.com/van1164/Sunwu-s_Closet/blob/main/img/KakaoTalk_20221113_170527576.jpg?raw=true'
    elif idx== '3' : 
        lst = Recomand(result_item_detail_new,result_cody_detail,result_style,['상의','navy'],le2,le)
        photo_url= 'https://github.com/van1164/Sunwu-s_Closet/blob/main/img/KakaoTalk_20221113_161928184.jpg?raw=true'
    temp_list = []
    
    for a,b in lst:
        new_dic =dict()
        new_dic['photo'] = b
        new_dic['idx'] = a
        temp_list.append(new_dic)
    
    
    return {
        'prev_content': {'photo:':photo_url},
        'User_content':temp_list}


@router.get("/app/recommendation/{idx}", tags=["recommendation_app"])
async def into_recommend_closet(idx : str):
    if idx =='1':
        photo_url ='https://github.com/van1164/Sunwu-s_Closet/blob/main/img/KakaoTalk_20221113_145639673.jpg?raw=true'
    elif idx =='2':
        photo_url ='https://github.com/van1164/Sunwu-s_Closet/blob/main/img/KakaoTalk_20221113_170527576.jpg?raw=true'
    elif idx== '3' : 
        photo_url= 'https://github.com/van1164/Sunwu-s_Closet/blob/main/img/KakaoTalk_20221113_161928184.jpg?raw=true'
    return {
        'User_content':
            {'photo': photo_url,
             'info_url': 'https://www.musinsa.com/app/blackfriday/special'}}