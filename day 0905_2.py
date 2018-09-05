#결측값 처리 및 데이터 프레임 사용 연습

# from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import random
random.seed(999)

#표준정규분포, 평균(기댓값):0, 표준편차:1
pd.DataFrame()
pd.Series()
df=pd.DataFrame(np.random.randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])  #행(row),열(col) 이름
# print(df)
# print(type(df))
print(type(df['W']))

print(df.drop('E'))
print(df)
# df=df.drop('E')
print(df.shape)
print(df.loc['A'])
print(df.iloc[0])
print(df.loc[['A','B'],['X', 'Y']])

d={'A':[1,2,np.nan], 'B':[5,np.nan, np.nan],'C':[1,2,3]}
print(d)

df=pd.DataFrame(d)
print(df)
print(type(df))

#nan값을 가진 행 또는 열을 삭제하기
print(df.dropna())
print(df.dropna(axis=0))
print(df.dropna(axis=1))

#임계치 설정
print(df.dropna(thresh=1))
print(df.dropna(thresh=2))

print(df['A'].fillna(value="temp"))
print(df.fillna(value="temp"))

#A열에 대해서 na값을 A열의 평균으로 대체해라
df['A'].mean() #A열의 평균값
print(df['A'].fillna(value=df['A'].mean()))

