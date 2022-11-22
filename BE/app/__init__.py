from .routes import *
import pandas as pd
import numpy as np
from numpy import dot
from numpy.linalg import norm
from sklearn.preprocessing import LabelEncoder
import os
print(os.getcwdb())
#CSV 파일 가져오기
result_cody_detail = pd.read_csv('app/each_cody_detail_df.csv', encoding='UTF-8')
result_item_detail = pd.read_csv('app/each_item_detail_df.csv',encoding='UTF-8')
result_style = pd.read_csv('app/each_cody_df.csv', encoding='cp949')

#result_item_detail에 있는 Unnamed: 0 column을 삭제해주고 string형태로 되어있는 리스트를 정제해서 list로 만들고 dataframe에 추가한다
result_item_detail.drop(['Unnamed: 0'], axis=1, inplace=True)
final_final_list = []
for a,i in result_item_detail.iterrows():
  for j in i:
    new_list5 = []
    if j is not np.NaN:
      for k in j.replace('[', '').replace(']', '').replace('\'', '').split(','):
        new_list5.append(k.strip())
      final_final_list.append(new_list5)

result_item_detail_new = pd.DataFrame(final_final_list, columns = ['카테고리', '이름', '색깔', '사이트', '삭제'])
result_item_detail_new.drop(['삭제'], axis=1, inplace=True)

#result_cody_detail에서도 똑같이 Unnamed:0를 drop 시키고 알맞는 column을 할당시켜준다
result_cody_detail.drop(['Unnamed: 0'], axis=1, inplace=True)

#result_style에서도 Unnamed: 0를 drop 해주고 이것도 똑같이 replace로 정제후 split해서 리스트로 만들고 각 아이템별로 데이터프레임 row에 추가한다
result_style.drop(['Unnamed: 0'], axis=1, inplace=True)
final_list = []
new_list = []
for a,i in result_style.iterrows():
  if (a+1) %2 == 1:
    new_list.append(i[0])
  if (a+1) % 2 == 0:
    for j in i[0].replace('[', '').replace(']', '').replace('\'', '').split(','):
      new_list.append(j.strip())
    final_list.append(new_list)
    new_list = []

#그러고 나서 알맞는 column name을 할당해준다.
brand_new_df = pd.DataFrame(final_list)
result_style = brand_new_df

le = LabelEncoder()
result_item_detail_new['카테고리'] = le.fit_transform(result_item_detail_new['카테고리'])
le2 = LabelEncoder()
result_item_detail_new['색깔'] = le2.fit_transform(result_item_detail_new['색깔'])
